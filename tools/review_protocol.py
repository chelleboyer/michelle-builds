"""Check review launch/handoff evidence; never launches agents or changes GitHub state.

Inputs are recorded evidence, not trusted attestation. See design/CODEX-WORKFLOW.md.
Python standard library only; no application/runtime dependency.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

LENSES = {
    "code": "Review correctness and requirement fulfillment; inspect actual source and consumers.",
    "seams": "Review contracts between producers and consumers, integration, and lifecycle boundaries.",
    "simplify": "Review unnecessary complexity against the accepted architecture and scope.",
    "tests": "Review validation quality and meaningful coverage under the recorded test-gap policy.",
    "errors": "Review failure handling, unavailable evidence, and silent failure paths.",
    "docs": "Review shipped documentation and operating instructions for accuracy and consistency.",
    "synthesis": "Verify specialist findings and evidence, reconcile prior findings and human deferrals; do not invent a replacement specialist review.",
}
REQUIRED = {"code", "seams", "simplify", "tests"}
PROTECTED = (
    "AGENTS.md", "PORTFOLIO-BRIEF.md", "context/", "design/ARCHITECTURE-ORCA.md",
    "design/CODEX-ASSIMILATION-PLAN.md", "design/CODEX-WORKFLOW.md",
    "tools/review_protocol.py", "templates/review-packet.json", "tests/protocol/", ".github/",
)
PACKET_KEYS = {
    "repository", "checkout", "pr", "base", "head", "merge_base", "round",
    "repair_rounds", "previous_review_head", "requirements", "human_decisions",
    "human_deferrals", "validation", "optional_lenses", "authorized_paths",
    "authorization_source", "repair_exception_source",
}
REVIEW_INSTRUCTIONS = """Independent read-only review. Work only in the specified checkout.
Read AGENTS.md, PORTFOLIO-BRIEF.md, context/MICHELLE-WORK-CATALOG.md,
design/ARCHITECTURE-ORCA.md, design/CODEX-WORKFLOW.md and every requirement reference.
Review the complete merge_base..head change and relevant consumers against the accepted
contract. Do not edit, commit, approve, merge, release, deploy, or post to GitHub.
Do not read parent conversations, session storage, memory, implementation reports,
other worktrees, or other specialist reports. Do not message another agent.
For synthesis only, the explicitly supplied specialist/prior reports are permitted.
Critical and Important defects block; Suggestions never block. Missing tests block
only for hard invariants or protected/security-sensitive behavior. On later rounds,
missing-test blockers must also be in code changed since previous_review_head.
Actual defects retain their normal severity. Preserve sourced human deferrals.
Report base/head, examined files and requirements, findings with stable IDs, severity,
evidence and disposition, limitations, and any unexpected/contaminating context.
No claim of independence or readiness substitutes for recorded launch evidence.
"""


class Invalid(ValueError):
    """The supplied evidence cannot establish readiness."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Invalid(message)


def exact(value: dict, keys: set[str], label: str) -> None:
    require(isinstance(value, dict) and set(value) == keys, f"{label}: unexpected/missing fields")


def strings(value: list, label: str, nonempty: bool = False) -> None:
    require(isinstance(value, list) and all(isinstance(x, str) and x.strip() for x in value), label)
    require(not nonempty or bool(value), f"{label}: empty")


def reference(value: str) -> bool:
    """Source coordinates only; provenance is still a human/agent audit obligation."""
    if not isinstance(value, str) or any(c.isspace() for c in value):
        return False
    if any(x in value.lower() for x in ("transcript", "rollout", "implementation-report", ".claude/reports", "session-storage")):
        return False
    return value.startswith(("https://", "user:")) or (
        not value.startswith("/") and ".." not in Path(value.split("#")[0]).parts
        and value.split("#")[0].endswith(".md")
    )


def sha(value: str) -> bool:
    return isinstance(value, str) and re.fullmatch(r"[0-9a-f]{40}", value) is not None


def digest(message: str) -> str:
    return hashlib.sha256(message.encode()).hexdigest()


def git(root: str, *args: str) -> str:
    return subprocess.check_output(["git", "-C", root, *args], text=True).strip()


def protected(path: str) -> bool:
    return any(path == p or (p.endswith("/") and path.startswith(p)) for p in PROTECTED) or any(
        part == ".env" or part.startswith(".env.") for part in Path(path).parts
    )


def packet_check(packet: dict) -> None:
    exact(packet, PACKET_KEYS, "packet allowlist")
    for name in ("repository", "checkout", "pr"):
        require(isinstance(packet[name], str) and bool(packet[name].strip()), name)
    for name in ("base", "head", "merge_base"):
        require(sha(packet[name]), name)
    require(packet["previous_review_head"] is None or sha(packet["previous_review_head"]), "previous_review_head")
    for name in ("round", "repair_rounds"):
        require(type(packet[name]) is int and packet[name] >= (1 if name == "round" else 0), name)
    require(packet["round"] == 1 or packet["previous_review_head"] is not None, "later round requires previous full-review head")
    for name in ("requirements", "human_decisions", "human_deferrals", "validation", "authorized_paths"):
        strings(packet[name], name, name in {"requirements", "validation"})
    for name in ("requirements", "human_decisions", "human_deferrals"):
        require(all(reference(x) for x in packet[name]), f"{name}: source references only, no conversation/report text")
    for name in ("authorization_source", "repair_exception_source"):
        require(packet[name] == "" or reference(packet[name]), f"{name}: source reference required")
    exact(packet["optional_lenses"], {"errors", "docs"}, "optional lenses")
    for value in packet["optional_lenses"].values():
        exact(value, {"required", "reason"}, "lens selection")
        require(type(value["required"]) is bool and isinstance(value["reason"], str) and bool(value["reason"].strip()), "lens reason required")
    for name in ("authorization_source", "repair_exception_source"):
        require(isinstance(packet[name], str), name)
    require(not packet["authorized_paths"] or bool(packet["authorization_source"].strip()), "protected paths need sourced human authorization")
    require(packet["repair_rounds"] <= 2 or bool(packet["repair_exception_source"].strip()), "stop: third repair requires explicit human exception")
    # These are paths, not policy globs. Approval is specific to this candidate.
    require(all(not x.startswith("/") and ".." not in Path(x).parts and not any(c in x for c in "*?[") for x in packet["authorized_paths"]), "authorization must name exact relative paths")


def required_lenses(packet: dict) -> set[str]:
    return REQUIRED | {k for k, v in packet["optional_lenses"].items() if v["required"]}


def checkout_check(packet: dict) -> None:
    root = packet["checkout"]
    require(git(root, "rev-parse", "HEAD") == packet["head"], "stale checkout head")
    require(not git(root, "status", "--porcelain", "--untracked-files=all"), "review checkout is dirty")
    require(git(root, "merge-base", packet["base"], packet["head"]) == packet["merge_base"], "merge-base mismatch")
    changed = git(root, "diff", "--name-only", "--no-renames", packet["merge_base"], packet["head"]).splitlines()
    denied = [p for p in changed if protected(p) and p not in packet["authorized_paths"]]
    require(not denied, f"protected changes lack explicit authorization: {denied}")


def launch(packet: dict, role: str, attempt: int, reports: list[str]) -> dict:
    packet_check(packet)
    require(role in required_lenses(packet) | {"synthesis"}, "unexpected review role")
    require(type(attempt) is int and attempt >= 1, "attempt")
    strings(reports, "reports")
    require(role == "synthesis" or not reports, "specialist packet must not carry other reports")
    require(role != "synthesis" or bool(reports), "synthesis requires specialist evidence")
    task = f"review_{re.sub('[^a-z0-9]+', '_', packet['pr'].lower()).strip('_')}_{packet['head'][:12]}_{packet['round']}_{role}_{attempt}"
    content = {"role": role, "packet": packet, "reports": reports}
    message = REVIEW_INSTRUCTIONS + "\nLens: " + LENSES[role] + "\n" + json.dumps(content, sort_keys=True, indent=2)
    return {"task_name": task, "fork_turns": "none", "message": message}


def receipt_check(receipt: dict, packet: dict, used: set[str]) -> str:
    exact(receipt, {"role", "attempt", "reports", "tool", "call", "agent_id", "packet_sha256", "later_messages"}, "launch receipt")
    require(receipt["tool"] == "collaboration.spawn_agent", "unsupported creation mechanism")
    expected = launch(packet, receipt["role"], receipt["attempt"], receipt["reports"])
    require(receipt["call"] == expected, "actual launch differs from allowlisted fresh launch")
    agent = receipt["agent_id"]
    require(isinstance(agent, str) and agent.endswith("/" + expected["task_name"]) and agent not in used, "missing/reused agent identity")
    require(receipt["packet_sha256"] == digest(expected["message"]), "packet hash mismatch")
    require(receipt["later_messages"] == [], "later messages contaminate the review")
    used.add(agent)
    return agent


def handoff_check(record: dict, live_head: str, used: set[str]) -> None:
    exact(record, {"action", "packet", "reviews", "validation", "findings", "synthesis"}, "handoff")
    require(record["action"] == "handoff", "agents cannot approve, merge, release, or deploy")
    packet = record["packet"]
    packet_check(packet)
    require(live_head == packet["head"], "stale PR head")
    checkout_check(packet)
    require(isinstance(record["reviews"], list), "reviews")
    require(len(record["reviews"]) == len(required_lenses(packet)), "missing/extra reviewers")
    roles = set()
    for review in [*record["reviews"], record["synthesis"]]:
        exact(review, {"receipt", "head", "report", "report_sha256", "contaminated", "complete"}, "review evidence")
        role = review["receipt"]["role"]
        require(role not in roles, "duplicate reviewer role")
        roles.add(role)
        receipt_check(review["receipt"], packet, used)
        require(review["head"] == live_head, "stale review head")
        require(review["contaminated"] is False and review["complete"] is True, "review incomplete/contaminated")
        report = Path(review["report"])
        require(report.is_file() and bool(report.read_text().strip()), "missing review report")
        require(digest(report.read_text()) == review["report_sha256"], "review report changed")
    require({r["receipt"]["role"] for r in record["reviews"]} == required_lenses(packet), "required lens missing")
    require(record["synthesis"]["receipt"]["role"] == "synthesis", "independent synthesis missing")
    supplied = set(record["synthesis"]["receipt"]["reports"])
    require({r["report"] for r in record["reviews"]} <= supplied, "synthesis missing specialist reports")
    require(isinstance(record["validation"], list), "validation")
    require(len(record["validation"]) == len(packet["validation"]), "missing validation")
    commands = []
    for result in record["validation"]:
        exact(result, {"command", "head", "exit_code", "evidence"}, "validation result")
        require(result["head"] == live_head and type(result["exit_code"]) is int and result["exit_code"] == 0, "failed/unavailable/stale validation")
        require(Path(result["evidence"]).is_file() and bool(Path(result["evidence"]).read_text().strip()), "validation evidence missing")
        commands.append(result["command"])
    require(sorted(commands) == sorted(packet["validation"]), "validation coverage mismatch")
    require(isinstance(record["findings"], list), "findings")
    ids = set()
    for finding in record["findings"]:
        exact(finding, {"id", "severity", "disposition", "evidence", "human_source"}, "finding")
        require(isinstance(finding["id"], str) and bool(finding["id"]) and finding["id"] not in ids, "finding ID")
        ids.add(finding["id"])
        require(finding["severity"] in {"Critical", "Important", "Suggestion"}, "severity")
        require(finding["disposition"] in {"open", "fixed", "disproved", "human-deferred"}, "disposition")
        require(isinstance(finding["evidence"], str) and bool(finding["evidence"].strip()), "finding evidence")
        if finding["disposition"] == "human-deferred":
            require(finding["human_source"] in packet["human_deferrals"], "deferral needs recorded human source")
        require(not (finding["severity"] in {"Critical", "Important"} and finding["disposition"] == "open"), "unresolved blocking finding")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    prepare = sub.add_parser("launch", help="print a checked spawn_agent call; does not execute it")
    prepare.add_argument("packet", type=Path)
    prepare.add_argument("role", choices=LENSES)
    prepare.add_argument("--attempt", type=int, default=1)
    prepare.add_argument("--report", action="append", default=[])
    check = sub.add_parser("handoff", help="check recorded evidence against a freshly read GitHub head")
    check.add_argument("record", type=Path)
    check.add_argument("--live-head", required=True)
    check.add_argument("--used-agents", type=Path, required=True, help="JSON array of earlier agent identities, including implementers")
    args = parser.parse_args()
    try:
        if args.command == "launch":
            packet = json.loads(args.packet.read_text())
            packet_check(packet)
            checkout_check(packet)
            result = launch(packet, args.role, args.attempt, args.report)
        else:
            used = json.loads(args.used_agents.read_text())
            strings(used, "used-agents")
            handoff_check(json.loads(args.record.read_text()), args.live_head, set(used))
            result = {"ready_for_human_review": True, "approved": False, "merged": False}
        print(json.dumps(result, indent=2))
        return 0
    except (Invalid, OSError, ValueError, KeyError, TypeError, subprocess.CalledProcessError) as error:
        print(f"REVIEW_PROTOCOL_BLOCKED: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
