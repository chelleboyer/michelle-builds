"""Behavioral regression cases using a real scratch Git repository and reports."""
from copy import deepcopy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[2] / "tools/review_protocol.py"
spec = importlib.util.spec_from_file_location("review_protocol", SCRIPT)
p = importlib.util.module_from_spec(spec)
spec.loader.exec_module(p)


class ProtocolTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.repo = self.root / "repo"
        self.repo.mkdir()
        self.git("init", "-q")
        self.git("config", "user.name", "Fixture")
        self.git("config", "user.email", "fixture@example.invalid")
        (self.repo / "file.txt").write_text("before\n")
        self.git("add", ".")
        self.git("commit", "-qm", "base")
        base = self.git("rev-parse", "HEAD")
        (self.repo / "file.txt").write_text("after\n")
        self.git("commit", "-qam", "candidate")
        self.head = self.git("rev-parse", "HEAD")
        self.packet = {
            "repository": "https://github.com/example/project", "checkout": str(self.repo),
            "pr": "42", "base": base, "head": self.head, "merge_base": base,
            "round": 1, "repair_rounds": 0, "previous_review_head": None,
            "requirements": ["design/approved.md"], "human_decisions": [], "human_deferrals": [],
            "validation": ["project-check"], "optional_lenses": {
                "errors": {"required": True, "reason": "error paths changed"},
                "docs": {"required": True, "reason": "operating instructions changed"}},
            "authorized_paths": [], "authorization_source": "", "repair_exception_source": "",
        }
        log = self.root / "validation.log"
        log.write_text("Real fixture check output\n")
        reviews = [self.review(role) for role in sorted(p.required_lenses(self.packet))]
        self.record = {"action": "handoff", "packet": self.packet, "reviews": reviews,
                       "synthesis": self.review("synthesis", [r["report"] for r in reviews]),
                       "validation": [{"command": "project-check", "head": self.head,
                                       "exit_code": 0, "evidence": str(log)}], "findings": []}

    def git(self, *args):
        return subprocess.check_output(["git", "-C", str(self.repo), *args], text=True).strip()

    def review(self, role, reports=None):
        reports = reports or []
        call = p.launch(self.packet, role, 1, reports)
        report = self.root / f"{role}.md"
        report.write_text(f"{role} reviewed {self.head}\n")
        return {"receipt": {"role": role, "attempt": 1, "reports": reports,
                            "tool": "collaboration.spawn_agent", "call": call,
                            "agent_id": "/root/" + call["task_name"],
                            "packet_sha256": p.digest(call["message"]), "later_messages": []},
                "head": self.head, "report": str(report), "report_sha256": p.digest(report.read_text()),
                "contaminated": False, "complete": True}

    def check(self, record=None, head=None, used=None):
        p.handoff_check(record or self.record, head or self.head, used or set())

    def test_complete_handoff_is_only_ready_for_human(self):
        self.check()
        record = self.root / "handoff.json"
        record.write_text(json.dumps(self.record))
        used = self.root / "used.json"
        used.write_text("[]")
        result = subprocess.run([sys.executable, str(SCRIPT), "handoff", str(record),
                                 "--live-head", self.head, "--used-agents", str(used)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout), {"ready_for_human_review": True, "approved": False, "merged": False})

    def test_inherited_or_omitted_context_is_refused(self):
        for value in [None, "all", "1", 1]:
            with self.subTest(value=value), self.assertRaises(p.Invalid):
                record = deepcopy(self.record)
                call = record["reviews"][0]["receipt"]["call"]
                if value is None:
                    del call["fork_turns"]
                else:
                    call["fork_turns"] = value
                self.check(record)

    def test_new_identity_does_not_make_resume_or_fork_independent(self):
        for method in ["collaboration.followup_task", "thread/fork", "thread/resume", "codex review"]:
            with self.subTest(method=method), self.assertRaises(p.Invalid):
                record = deepcopy(self.record)
                record["reviews"][0]["receipt"]["tool"] = method
                self.check(record)

    def test_earlier_agent_identity_is_refused(self):
        with self.assertRaisesRegex(p.Invalid, "reused"):
            self.check(used={self.record["reviews"][0]["receipt"]["agent_id"]})

    def test_missing_launch_and_changed_packet_are_refused(self):
        for key in ["call", "packet_sha256"]:
            with self.subTest(key=key), self.assertRaises(p.Invalid):
                record = deepcopy(self.record)
                del record["reviews"][0]["receipt"][key]
                self.check(record)
        self.record["reviews"][0]["receipt"]["call"]["message"] += "\nImplementer says this is fine."
        with self.assertRaises(p.Invalid):
            self.check()

    def test_transcript_fields_and_text_in_source_slots_are_refused(self):
        for key in ["transcript", "conversation", "implementation_report", "compaction_summary"]:
            with self.subTest(key=key), self.assertRaises(p.Invalid):
                packet = deepcopy(self.packet)
                packet[key] = "parent history"
                p.launch(packet, "code", 1, [])
        for value in ["The implementer said this was correct", ".claude/reports/implementation.md", "session-transcript.md"]:
            with self.subTest(value=value), self.assertRaises(p.Invalid):
                packet = deepcopy(self.packet)
                packet["requirements"] = [value]
                p.launch(packet, "code", 1, [])

    def test_specialist_cannot_receive_other_reports(self):
        with self.assertRaises(p.Invalid):
            p.launch(self.packet, "code", 1, ["tests.md"])

    def test_later_messages_and_context_contamination_block(self):
        self.record["reviews"][0]["receipt"]["later_messages"] = ["parent commentary"]
        with self.assertRaises(p.Invalid):
            self.check()
        self.record["reviews"][0]["receipt"]["later_messages"] = []
        self.record["reviews"][0]["contaminated"] = True
        with self.assertRaises(p.Invalid):
            self.check()

    def test_stale_live_head_review_and_validation_each_block(self):
        with self.assertRaisesRegex(p.Invalid, "stale PR"):
            self.check(head=self.packet["base"])
        for field in ["reviews", "validation"]:
            with self.subTest(field=field), self.assertRaises(p.Invalid):
                record = deepcopy(self.record)
                record[field][0]["head"] = self.packet["base"]
                self.check(record)

    def test_missing_failed_and_changed_reports_block(self):
        for mode in ["missing-role", "failed", "deleted-report", "changed-report"]:
            with self.subTest(mode=mode), self.assertRaises(p.Invalid):
                record = deepcopy(self.record)
                report = Path(record["reviews"][0]["report"])
                original = report.read_text()
                try:
                    if mode == "missing-role": record["reviews"].pop()
                    elif mode == "failed": record["reviews"][0]["complete"] = False
                    elif mode == "deleted-report": report.unlink()
                    else: report.write_text("Different findings")
                    self.check(record)
                finally:
                    report.write_text(original)

    def test_missing_or_nonindependent_synthesis_blocks(self):
        self.record["synthesis"] = deepcopy(self.record["reviews"][0])
        with self.assertRaises(p.Invalid):
            self.check()

    def test_failed_unavailable_and_missing_checks_block(self):
        for code in [1, None, False]:
            with self.subTest(code=code), self.assertRaises(p.Invalid):
                record = deepcopy(self.record)
                record["validation"][0]["exit_code"] = code
                self.check(record)
        self.record["validation"] = []
        with self.assertRaises(p.Invalid):
            self.check()

    def test_dirty_or_wrong_checkout_blocks(self):
        (self.repo / "untracked.txt").write_text("not part of candidate")
        with self.assertRaisesRegex(p.Invalid, "dirty"):
            self.check()
        (self.repo / "untracked.txt").unlink()
        self.git("checkout", "--detach", self.packet["base"])
        with self.assertRaisesRegex(p.Invalid, "stale checkout"):
            self.check()

    def test_protected_change_requires_exact_sourced_authorization(self):
        (self.repo / "AGENTS.md").write_text("Human-owned rules")
        self.git("add", ".")
        self.git("commit", "-qm", "protected change")
        self.packet["head"] = self.git("rev-parse", "HEAD")
        with self.assertRaisesRegex(p.Invalid, "protected changes"):
            p.checkout_check(self.packet)
        self.packet["authorized_paths"] = ["AGENTS.md"]
        with self.assertRaises(p.Invalid):
            p.packet_check(self.packet)
        self.packet["authorization_source"] = "user:2026-09-21/approved-assimilation"
        p.packet_check(self.packet)
        p.checkout_check(self.packet)
        self.packet["authorized_paths"] = ["*"]
        with self.assertRaises(p.Invalid):
            p.packet_check(self.packet)

    def test_third_repair_stops_without_scoped_human_exception(self):
        self.packet["repair_rounds"] = 3
        with self.assertRaisesRegex(p.Invalid, "third repair"):
            p.launch(self.packet, "code", 1, [])
        self.packet["repair_exception_source"] = "user:2026-09-21/one-off-third-repair"
        p.launch(self.packet, "code", 1, [])

    def test_later_review_requires_previous_full_head(self):
        self.packet["round"] = 2
        with self.assertRaises(p.Invalid):
            p.packet_check(self.packet)

    def test_blockers_suggestions_and_human_deferrals_remain_distinct(self):
        finding = {"id": "R1", "severity": "Suggestion", "disposition": "open", "evidence": "file:1", "human_source": ""}
        self.record["findings"] = [finding]
        self.check()
        finding["severity"] = "Important"
        with self.assertRaisesRegex(p.Invalid, "blocking"):
            self.check()
        finding["disposition"] = "human-deferred"
        with self.assertRaisesRegex(p.Invalid, "deferral"):
            self.check()
        source = "user:2026-09-21/defer-R1"
        self.packet["human_deferrals"] = [source]
        finding["human_source"] = source
        # Changed human decisions require new sessions/packets, not reused evidence.
        with self.assertRaises(p.Invalid):
            self.check()

    def test_sourced_deferral_passes_with_new_complete_review(self):
        source = "user:2026-09-21/defer-R1"
        self.packet["human_deferrals"] = [source]
        reviews = [self.review(role) for role in sorted(p.required_lenses(self.packet))]
        self.record["reviews"] = reviews
        self.record["synthesis"] = self.review("synthesis", [r["report"] for r in reviews])
        self.record["findings"] = [{"id": "R1", "severity": "Important",
                                    "disposition": "human-deferred", "evidence": "file:1",
                                    "human_source": source}]
        self.check()
        self.assertEqual(self.record["findings"][0]["disposition"], "human-deferred")

    def test_agents_cannot_approve_merge_release_or_deploy(self):
        for action in ["approve", "merge", "release", "deploy"]:
            with self.subTest(action=action), self.assertRaises(p.Invalid):
                record = deepcopy(self.record)
                record["action"] = action
                self.check(record)

    def test_launch_cli_refuses_bad_packet_with_nonzero_exit(self):
        self.packet["conversation"] = "parent transcript"
        file = self.root / "bad.json"
        file.write_text(json.dumps(self.packet))
        result = subprocess.run([sys.executable, str(SCRIPT), "launch", str(file), "code"], capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("REVIEW_PROTOCOL_BLOCKED", result.stderr)
        self.assertEqual(result.stdout, "")


if __name__ == "__main__":
    unittest.main()
