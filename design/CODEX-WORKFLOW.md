# Codex operating protocol

This implements the [approved assimilation plan](CODEX-ASSIMILATION-PLAN.md),
including its fresh-session clarification. Michelle authorized implementation in
the task conversation on 2026-09-21. Work Unit 5 remains paused until she separately
resumes it. Nothing here authorizes approval, merge, release, or deployment.

## Authority and required context

Read `AGENTS.md`, `PORTFOLIO-BRIEF.md`, `context/MICHELLE-WORK-CATALOG.md`, this
protocol, the approved `design/ARCHITECTURE-ORCA.md`, and the work item's accepted
requirements. The brief owns product intent; the catalog owns factual claims and
publication boundaries; approved architecture owns the site structure; `AGENTS.md`
and this document own process. Surface contradictions instead of resolving them
by rewriting a source. Current explicit human instructions constrain the task.

Generic skills are helpers. Their approval, merge, deployment, inherited-review,
or unlimited repair steps cannot override this protocol. No framework, application
runtime dependency, Archon installation, scheduler, or unattended loop is added.

## Work lifecycle

1. **Triage:** verify the issue/request against current source and tracker state.
   State the problem, why it matters, why now, desired outcome, invariants, and
   acceptance evidence. Investigate an unproven cause; plan unresolved design;
   stop for a new architecture/governance decision. An approved request may be
   the work item; do not invent an issue number or publish a backlog without the
   human publication gate.
2. **Implement:** use one branch/worktree and one PR per accepted work item.
   Preserve human and reviewer edits, including untracked work. Adjacent findings
   are surfaced separately; they do not expand the issue automatically.
3. **Validate:** run every applicable check and retain actual exit codes and
   nonempty evidence at the candidate head. A strict build does not prove runtime,
   browser, accessibility, or editorial correctness. Required but unavailable
   checks block readiness. Use synthetic inputs and only scratch resources owned
   by the run. Never pipe a failing command into a successful log-filter command
   and report the latter's exit as the check result.
4. **Draft PR:** describe the actual problem/outcome and complete resulting change.
   Keep it draft until the independent review, validation, and evidence gate pass.
   Link the source work item. Include assumptions, limitations, deferrals, and
   protected-path authorization. Do not turn a PR-body wording requirement into
   an impossible code-repair criterion; edit the body as its own handoff step.
5. **Independent review:** run the required fresh specialist sessions and then a
   fresh synthesis session as specified below. They review the complete change
   against the approved contract, not an implementer's summary.
6. **Repair:** repair findings in scope, validate the complete resulting change,
   and perform another fresh full review. Count repair passes at PR level across
   sessions, including human-requested repair passes. Two are permitted. Before a
   third, stop and return findings to Michelle. Only a sourced, scoped human
   exception permits another pass; it does not change the standing limit.
7. **Human handoff:** verify live PR head, checks, evidence, coverage, and findings.
   Mark ready only after the gate passes. Ready means ready for Michelle's review,
   never approved. Michelle performs acceptance, merge, and release. Read actual
   GitHub state; a request to merge, local green checks, or code existing does not
   establish a merged or shipped state.

For changes to a screen, route, or navigation entry, the PR answers: primary
object; primary action; taps/clicks to reach it; removable screens; removable
navigation levels; optional fields; concepts that are one object; and whether
technical complexity leaks into the UI. Quote changed public copy for human
editorial review. Factual/publication restrictions remain those of the catalog.

## Protected decisions and paths

Explicit, scoped human authorization is required for edits to:

- `AGENTS.md`, `PORTFOLIO-BRIEF.md`, `context/`.
- `design/ARCHITECTURE-ORCA.md`, `design/CODEX-ASSIMILATION-PLAN.md`, this protocol.
- `tools/review_protocol.py`, `templates/review-packet.json`, `tests/protocol/`,
  `.github/`, and any `.env` file.

The approved assimilation authorizes this protocol, the focused AGENTS update,
and its checker/tests. It does not authorize subsequent agents to tune their own
judge. Document exact authorized changed paths and the human source. New public
facts, lifecycle promotions, architecture changes, release choices, credentials,
real-data operations, and deployment remain human decisions. Do not weaken tests
or alter requirements to make a check pass. Never read or publish secrets.

A recorded authorization source is evidence to inspect, not machine-verifiable
human identity. The local checker cannot prevent a direct tool call or dishonest
record. Worktrees isolate checkouts, not credentials or filesystem reads.

## Roles and required review coverage

| Role | Responsibility |
| --- | --- |
| Implementer | Bounded code/document changes and factual validation evidence. No self-approval. |
| Code reviewer | Correctness, accepted requirements, and relevant callers/consumers. |
| Seams reviewer | Cross-file contracts, integration, state/lifecycle ownership. |
| Simplicity reviewer | Complexity justified by the accepted architecture and scope. |
| Tests reviewer | Tests that prove meaningful behavior and applicable validation coverage. |
| Errors reviewer | Required when failure-handling paths change; explain inclusion/exclusion. |
| Docs reviewer | Required when shipped documentation or operating instructions change; explain inclusion/exclusion. |
| Synthesizer | Fresh independent session; verify findings, deduplicate, preserve disagreement and human deferrals, and record coverage. |
| Runtime/holdout verifier | Where required by the accepted work, verify actual candidate identity and observable behavior in fresh scratch environments. |

Code, seams, simplicity, and tests always run. Optional lens decisions and reasons
are recorded before launch. Review in batches when slots are limited; never combine
required roles because of capacity. A failed reviewer is replaced by a newly
created session, not resumed or silently omitted. Missing enabled reports block.

Critical and Important defects block; Suggestions never block. A missing/weak test
is Important only for an AGENTS hard invariant or a protected/security-sensitive
behavior. First review lists all gaps. Later test-gap blockers must also concern
code changed since the previous full-review head. Gaps in already-reviewed code
are Suggestions. Actual demonstrated defects retain their ordinary severity.
Human deferrals require their source and remain labeled deferred, not fixed.

## Fresh-session procedure

Use only the current host's `collaboration.spawn_agent` with explicit
`fork_turns: "none"`. Do not use the default, numeric inheritance, `all`, resume,
fork, or `followup_task` to create/reuse a reviewer. Do not forward implementer
conversation, compaction summaries, rationale, or implementation reports.
If this exact host mechanism is absent, stop. There is no implicit CLI/Archon fallback.

1. Commit the candidate and prepare a clean detached review checkout at its SHA.
   Resolve base and merge-base and record the actual PR identity. Do not review
   the implementer's paused/dirty workspace.
2. Copy [the packet template](../templates/review-packet.json) to an evidence
   directory **outside the repository** and fill source references and exact
   SHAs. `user:<date>/<decision>` identifies a human instruction in the task
   conversation; the coordinator must verify it, not send the entire conversation.
   Requirement files are authoritative inputs. Do not relabel an implementation
   summary as a requirement. Review the packet's meaning as well as its shape.
3. Prepare a launch, preserving the unfiltered exit status:

   ```bash
   python3 tools/review_protocol.py launch /path/to/packet.json code
   ```

   The command checks the clean pinned checkout and protected paths, and prints
   the exact `task_name`, `fork_turns`, and `message` for the tool call. It does not
   dispatch. Repeat for each selected role. Use `--attempt 2` for a replacement,
   never reuse the old identity. Record the printed call verbatim before dispatch.
4. Invoke the collaboration tool with exactly that object. Record the actual tool
   name, call, returned agent identity, and SHA-256 of the UTF-8 `message` (not the
   outer JSON). Keep a cumulative list of prior/implementer agent identities
   across rounds and compare against it. No follow-up messages are permitted;
   changed input requires a new packet and session.
5. The reviewer checks source coordinates, reads complete requirements and source,
   and returns its report to the coordinator. Save its returned report unchanged
   outside the repository. Reviewer agents do not edit files or post to GitHub.
   Reports identify role, base/head, files/requirements examined, findings with
   stable IDs/severity/evidence/disposition, limitations, and unexpected context.
6. After every specialist finishes, launch **synthesis** with the same mechanism
   and `--report /path/to/report.md` for each specialist; prior findings may be
   supplied here for reconciliation. All required specialist reports must be
   supplied. The synthesizer verifies findings against source and applicable
   proof, records each required agent identity and coverage, and preserves sourced
   human decisions. Implementation reports are never specialist inputs.
7. Save the handoff evidence using the shape below, and run:

   ```bash
   python3 tools/review_protocol.py handoff /path/to/handoff.json \
     --live-head <freshly-read-GitHub-PR-head> \
     --used-agents /path/to/earlier-agent-identities.json
   ```

   Exit 0 is ready for human review only. Any error blocks readiness. Append the
   current agent identities to the cumulative record after the review; retain
   failed attempts too. Check GitHub head again before marking ready; any new
   commit requires new validation and independent sessions. Actual launch
   observations, human-source authenticity, and complete semantic coverage are
   audited by the coordinator and Michelle, not certified by a JSON file.

### Evidence shapes

The packet template lists the complete field allowlist. References in
`requirements`, `human_decisions`, and `human_deferrals` are document paths,
HTTPS source links, or `user:` decision coordinates, not conversation text.
Optional lenses each have `required` and `reason`. `authorized_paths` names exact
changed paths; wildcards are refused. `authorization_source` and
`repair_exception_source` are empty unless an applicable human decision exists.

A launch receipt has exactly these fields:

```json
{
  "role": "code", "attempt": 1, "reports": [],
  "tool": "collaboration.spawn_agent",
  "call": {"task_name": "...", "fork_turns": "none", "message": "..."},
  "agent_id": "/root/...", "packet_sha256": "...", "later_messages": []
}
```

Each review record contains `receipt`, `head`, `report` (a path),
`report_sha256` (UTF-8 report text), `contaminated: false`, and `complete: true`.
The handoff object contains exactly:

- `action: "handoff"`, the original `packet`, `reviews` (specialist records), and
  `synthesis` (its separate review record).
- `validation`: one result per packet command, each with `command`, `head`,
  `exit_code`, and nonempty `evidence` file path. Unavailable checks do not pass.
- `findings`: records with `id`, `severity`, `disposition` (`open`, `fixed`,
  `disproved`, or `human-deferred`), `evidence`, and `human_source` (empty unless
  deferred; otherwise one of the packet's recorded deferral references).

Keep raw logs, exact calls, responses, packets, hashes, and reports outside the
repository; summarize pertinent results in the PR. Do not publish transcripts,
private reference code, credentials, or internal environment details. Missing,
changed, contaminated, or stale evidence blocks the handoff.

## Verification and limits

Run the protocol regression suite, then the existing static-site checks:

```bash
python3 -m unittest discover -s tests/protocol -v
python -m pip check
python -m mkdocs build --strict
```

The regression suite exercises refusal of unsafe launch inputs, reused identities,
stale evidence, missing required roles, failed validation, unauthorized protected
changes, and a third repair without explicit authorization. It also checks that
Suggestions do not block and human deferrals remain sourced. These tests are
local explicit validation; they do not install hooks or unattended automation.

`fork_turns: "none"` controls conversation forwarding, not filesystem isolation.
Agents must not read session storage, conversational memory, other worktrees, or
implementation reports to reconstruct history. Encountering material unauthorized
context invalidates the review and requires a new session after correcting inputs.
System/developer instructions, repository guidance, and model remain shared.

The approved plan records the actual one-off marker probes, including the
inconclusive inherited-context control. No raw model payload was inspected.
The guarantee is the tool's explicit no-forwarding contract and recorded call;
marker behavior corroborates it but is not exhaustive proof. Repeat the probe
when changing host/session mechanism, with an explicitly supplied marker as the
positive detection control. A stronger raw-payload proof requirement stops work
until Michelle decides how to satisfy it. Do not claim it has been verified.

The checker never contacts GitHub, launches tools/agents, grants authorization,
changes PR state, or enforces an OS sandbox. It rejects inconsistent evidence
supplied to it. Packet semantics, provenance, complete findings, required check
selection, truthful repair counts, and human authority still require inspection.
Do not represent these procedural obligations as tamper-proof enforcement.
