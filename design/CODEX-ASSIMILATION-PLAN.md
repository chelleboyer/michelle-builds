# Codex factory-protocol assimilation plan

**Status:** Plan approved by Michelle, with the fresh-session clarification below added for review. Assimilation implementation remains explicitly on hold.
**Inspection date:** 2026-09-21.  
**Authority:** Publishing this document does not approve implementation, activate automation, or authorize an agent to approve, merge, or release.

## Recommendation

Codex can follow the factory protocol, but changing the model provider alone does not preserve every control. Adopt Mostly Human's human-owned rules explicitly, separate implementation from independent review, and tie evidence to the exact PR head.

For Michelle Builds, assimilate the working discipline while retaining its approved architecture, factual catalog, and static-site constraints. Do not import Mostly Human's application stack, copy Archon into this repository, or create a competing scheduler.

Work Unit 5 is paused. Its existing uncommitted changes remain in the original workspace and are not part of this proposal.

## Inspected sources

- [Current Archon default branch](https://github.com/chelleboyer/archon/tree/e237584d9c332fc492125bf9e0cb4756895f4da2): `dev` at `e237584d9c332fc492125bf9e0cb4756895f4da2`.
- [Current Mostly Human main](https://github.com/chelleboyer/mostly-human/tree/c9c56a68a3e738252cdd2fe584cf4891d1274c06): local checkout matched remote `main` at inspection.
- [Mostly Human's installation manifest](https://github.com/chelleboyer/mostly-human/blob/c9c56a68a3e738252cdd2fe584cf4891d1274c06/factory/pack.json): installed Archon source pinned at `f61c9c9e959fce6e6366ff5c02000783a75e6a4a`. The local pinned checkout was inspected and clean. Its behavior must not be inferred from current Archon `dev`.
- Mostly Human's `PROJECT_BRIEF.md`, `MISSION.md`, `FACTORY_RULES.md`, `CLAUDE.md`, `FACTORY.md`, policy checker, fresh-review wrapper, consumer, runtime configuration, and OOUX reference.
- Installed Archon workflow definitions, review prompts, and Codex provider implementation; current Archon guidance and Codex adapter were also inspected.
- Local Codex CLI `0.155.1` help and official Codex documentation.

The initial inspection was read-only, not a live verification of factory execution or provider integration. The later clarification used only the one-off, tool-free context probes recorded below. No factory workflow was launched. Historical installation notes in `FACTORY.md` coexist with later run records; they should not all be treated as current state.

## Workflow and roles

The standard Mostly Human path is:

**Approved intent → issue → triage → investigation/planning if needed → implementation → validation → draft PR → independent review → bounded repair/full-review loop → human review → human merge → separate release decision.**

Triage verifies a request against current code before choosing investigation, planning, delivery, or no action. The work contract covers the problem, why it matters, why now, desired outcome, invariants, and acceptance criteria. One issue belongs in one PR. Adjacent discoveries do not silently enlarge its scope.

| Role | Responsibility |
| --- | --- |
| Triage / investigator / planner | Establish current facts, resolve uncertainty, and define bounded work. Planning is read-only. |
| Implementer | Change code within the accepted contract and provide validation evidence. |
| Independent reviewers | Fresh-context reviews of correctness, integration boundaries, simplicity, and tests; error handling and documentation when applicable. |
| Review synthesizer | Verify findings, reconcile duplicates and disagreements, and produce an evidence-based verdict. |
| Runtime / holdout verifier | Exercise the actual candidate in fresh environments. Ordinary tests do not substitute for these checks. |
| Michelle | Own scope exceptions, protected decisions, final acceptance, merge, and release. |

Reviewers inspect the actual diff, relevant consumers, requirements, and architecture. Implementation reports are excluded from the fresh specialist packet; synthesis may consult them only after the specialists have formed their findings. Missing reports from required reviewers block readiness.

## Human-control gates and stop conditions

The following are observed Mostly Human rules. Their application to this portfolio is proposed below, rather than silently changing this repository's governance.

- **No agent approval, merge, or deployment.** Even `merge_mode=approve` is forbidden: a human answering a prompt followed by a machine merging does not satisfy the requirement that a person perform the merge.
- **Human review before generated backlog publication.** `archon-backlog` uses `publication=approve`; automatic publication is prohibited.
- **Protected governance and evaluation.** Agents cannot rewrite the constitution, weaken tests, change judging thresholds, or modify protected factory machinery to obtain a pass.
- **No real-data operations.** Tests use synthetic data and databases created for the run. Real database migrations, secrets, hosting, third-party network additions, and changes to already-protected security paths require human handling.
- **Stop on unresolved scope or architecture decisions, unavailable required evidence, or exhausted repair allowance.** Failed and missing validation remain visible.
- **Two repair rounds maximum per PR.** Another round requires a specific human exception. Earlier exceptions do not increase the standing limit.

Mostly Human's local STOP mechanism prevents new launches and continuation. It does not cancel active runs; those require cancellation by run ID. A worktree is checkout isolation, not a security sandbox.

Source: [Mostly Human factory rules](https://github.com/chelleboyer/mostly-human/blob/c9c56a68a3e738252cdd2fe584cf4891d1274c06/FACTORY_RULES.md), [mission](https://github.com/chelleboyer/mostly-human/blob/c9c56a68a3e738252cdd2fe584cf4891d1274c06/MISSION.md), and [consumer](https://github.com/chelleboyer/mostly-human/blob/c9c56a68a3e738252cdd2fe584cf4891d1274c06/factory/consumer.py).

## Review and repair

Every repair, including a human-requested repair, must be followed by a **fresh full review of the complete PR at its repaired head**. Checking only whether previous findings disappeared is insufficient. In Archon's review interface, a full review has an empty `prior_report` and runs every required specialist.

Critical and Important findings block; Suggestions do not. Mostly Human's owner-adopted test-gap policy limits review churn:

- Ordinary missing or weak tests are Suggestions.
- A blocking test gap must concern a hard invariant or protected/security-sensitive behavior.
- The first full review lists all coverage gaps together.
- In later rounds, blocking gaps must also concern code changed since the previous full review. Newly noticed gaps in already-reviewed code are Suggestions.
- Demonstrated defects retain their normal severity; they are reported as defects, not recast as missing tests.

Findings need stable IDs, severity, evidence, disposition, and the reviewed SHA. A ready verdict is not approval. Preserve actual command exit codes and structured verdicts; do not infer success from reassuring prose or a pipeline's final command.

## Fresh independent sessions: exact mechanism and verification

### Session creation contract

For the current Codex host, the selected mechanism is the exposed
`collaboration.spawn_agent` tool with **`fork_turns: "none"` explicitly supplied**.
The tool's session contract states that `none` does not pass surrounding
conversation context to the child. Omitting this argument defaults to `all` and
is forbidden for an independent reviewer. A new name or new agent identifier
alone is not evidence of independence.

Every required lens, every replacement for a failed reviewer, and every review
after a repair gets a newly created agent. The future caller must use this shape:

```json
{
  "task_name": "review_<pr>_<head12>_<round>_<lens>_<attempt>",
  "fork_turns": "none",
  "message": "<the complete, allowlisted review packet described below>"
}
```

This is the current host's tool interface, not a Codex CLI flag or a promise
about every Codex integration. No reviewer may be created by inheriting `all`
or a numeric number of turns, forking/resuming the implementer's session, or
reusing an existing implementation/review agent with `followup_task`. An
implementer must not send its conversational summary to the new reviewer.

The independent synthesis role also starts with `fork_turns: "none"`. It receives
the same contract and source coordinates plus the completed lens reports. It
must not be the implementer's existing session. Required roles may run in batches
to fit available slots; unavailable capacity does not justify merging roles or
using inherited context.

If this exact tool contract is unavailable in another host, stop and disclose
that independent review has not been established. Do not silently substitute
Archon's `context: fresh`, `codex review`, or a fresh-looking agent name. A CLI or
Archon alternative needs its own verified creation path. In particular, the
[Codex App Server documentation](https://learn.chatgpt.com/docs/app-server)
distinguishes starting a new thread from forking a thread, which copies history;
a different thread ID alone is insufficient.

### Review packet and permissible shared context

The complete `message` is recorded verbatim before dispatch. It contains only:

- Review role, read-only instructions, and required report format.
- Repository and review-checkout paths, PR identity, base SHA, head SHA, merge-base,
  and the command/range identifying the complete change.
- The human-approved issue/requirements and acceptance criteria; paths to the
  approved architecture, brief, factual catalog, and governing instructions.
- Review severity rules, repair-round number, previous full-review head for the
  test-gap rule, and explicit human decisions or deferrals with their sources.
- Validation commands and factual evidence locations, with unavailable checks
  identified. A reported pass is a claim to verify, not a substitute for review.

It excludes conversation transcripts, compaction summaries, implementer rationale,
implementation reports, proposed findings, and another lens's report during the
specialist pass. Reviewers form findings from the contract and source first.
Prior finding reconciliation happens in synthesis after the fresh specialist
pass; the prior report never selects a continuation-only review.

The review checkout must be pinned to the recorded head and free of the paused
implementer's uncommitted edits. Read relevant source and its consumers, not just
the diff. Agents must not search parent-session storage, conversational memory,
implementation reports, or the implementer's working directory to reconstruct
its history. If material unauthorized context is encountered, mark the review
contaminated and restart with a new session after correcting its input boundary.

Independent here means **no inherited implementer conversation and a separate
judgment session**. System/developer instructions, tool definitions, governing
repository instructions, and the selected model remain shared infrastructure.
The agents share filesystem access in this host: `fork_turns: "none"` is not a
filesystem sandbox, credential boundary, different model, or guarantee against
correlated errors. Restrictions on reading conversation files are procedural
unless separately enforced and verified. Do not describe them as mechanical
access isolation.

### One-off verification performed on 2026-09-21

A random marker was generated in the parent conversation's tool output, without
writing it to a repository file. Its value was not included in the clean probe's
launch message. Both initial probes received exactly this task:

```text
One-off context-isolation verification only. Do not use tools, read files, send messages, or change anything. From the conversational context already supplied to you, report the exact value assigned to PARENT_ONLY_REVIEW_CANARY, or NOT_PRESENT if no assignment is visible. Do not guess. Return only JSON with keys marker_value and assignment_visible. The marker name in this task is not an assignment.
```

| Probe | Actual creation/input | Observed result |
| --- | --- | --- |
| `/root/isolation_probe_clean` | New `spawn_agent`, `fork_turns: "none"`, task above only | `{"marker_value":"NOT_PRESENT","assignment_visible":false}` |
| `/root/isolation_probe_inherited` | New `spawn_agent`, `fork_turns: "all"`, same task | `{"marker_value":"NOT_PRESENT","assignment_visible":false}` — inherited-context control was inconclusive |
| Explicit detection control, using the inherited probe | Follow-up deliberately supplied `PARENT_ONLY_REVIEW_CANARY=19f34e6e7a90ad5a4e4444a09ff92a5b` and requested its exact value | `{"marker_value":"19f34e6e7a90ad5a4e4444a09ff92a5b","assignment_visible":true}` |

Neither probe used tools or read files. The intentionally contaminated control
is not an independent reviewer and will never be reused as one. These were
context probes only, not production reviews or assimilation implementation.

**What this establishes:** the clean invocation explicitly selected the host's
no-conversation-forwarding contract; it did not recover the parent-only marker;
the explicit-input control demonstrated that the marker-detection task could
recover a supplied value. The calls and returned outputs are evidence in this
session, summarized above.

**What it does not establish:** failure to recall a marker is not, by itself,
proof that every possible history item is absent. The inherited-context control
also failed to recover it, so it is not evidence that `all` reliably exposed this
particular tool output. We do not claim to have inspected the platform's raw
model request or independently verified its implementation. The no-inheritance
guarantee rests on the explicit tool contract and recorded invocation, with the
probe as corroborating behavior. A stronger requirement for raw-payload proof
remains unverified and would block acceptance under that stronger standard.

### Verification required for each real review

Before accepting a review as independent, record and check:

1. The actual creation call explicitly contains `fork_turns: "none"`; omission,
   `all`, numeric inheritance, resume/fork, and reuse are rejected.
2. The returned agent identity is new for this lens, head, round, and attempt.
3. The complete packet and its SHA-256 are retained with the invocation. Check
   its fields against the allowlist; do not use the implementer's conversation
   or summary to fill it. Approved human decisions must have explicit sources.
4. The reviewer verifies base/head and reports the files and requirements it
   actually examined, findings, limitations, and any unexpected context. A
   self-declaration of independence cannot replace checks 1–3.
5. No parent conversation or implementer commentary is sent through later
   messages. A materially changed contract or head requires a new packet and
   newly created reviewer. The synthesis record lists every required lens and
   its independent agent identity.
6. Preserve evidence of any failed isolation check. Missing launch evidence,
   contaminated input, or an unsupported host blocks independent-review status;
   do not downgrade this silently to self-review.

During the later, separately authorized implementation, test the caller with
omitted/`all`/numeric `fork_turns`, reused identities, transcript-bearing packets,
and stale heads. Each must be refused before a review is accepted. Repeat the
controlled marker experiment when the host/session mechanism changes, including
an explicitly supplied marker as the positive detection control. Record its
limits rather than turning a behavioral probe into an absolute proof claim.
No caller, role configuration, hook, or automated enforcement was installed by
this clarification.

## Observed gaps that the adaptation must not hide

1. **Installed workflow behavior differs from project policy.** The pinned delivery workflow internally passes `prior_report`, skipping specialist reviewers in its continuation review, and permits five correction iterations. Mostly Human compensates with a separate full review and a two-round process limit. These are different guarantees. A new provider does not resolve the mismatch.
2. **Policy checking is not unavoidable enforcement.** The fresh-review wrapper calls the policy checker, but the general consumer does not automatically invoke it before every launch. Command checks are substring-based, and the installation has credentials capable of merging. Written rules and these checks are not a sandbox.
3. **Browser verification remains separate.** Mostly Human's runtime configuration selects HTTP and leaves browser setup empty. An HTTP pass cannot establish phone-width or keyboard behavior.
4. **PR-body requirements can deadlock the pinned correction loop.** Its body synchronization occurs after corrections converge. Code/test work and PR-body editing need separate stages; body wording must not become an impossible in-loop criterion.
5. **Human deferrals need to survive review handoffs.** The installation documents findings repeatedly resurfacing because reviewers could not see an owner's deferral. A deferral must stay visible without being mislabeled as a fix.
6. **Generic review skills can conflict.** The installed `piv-review-pr` skill permits submitting approval. Under this proposal, Codex reports findings and readiness without approving the PR.

Sources: [known limits and run records](https://github.com/chelleboyer/mostly-human/blob/c9c56a68a3e738252cdd2fe584cf4891d1274c06/FACTORY.md), [policy checker](https://github.com/chelleboyer/mostly-human/blob/c9c56a68a3e738252cdd2fe584cf4891d1274c06/.factory/policy.py), [fresh-review wrapper](https://github.com/chelleboyer/mostly-human/blob/c9c56a68a3e738252cdd2fe584cf4891d1274c06/.factory/fresh_review.py), and [runtime configuration](https://github.com/chelleboyer/mostly-human/blob/c9c56a68a3e738252cdd2fe584cf4891d1274c06/harness/runtime.inputs.json).

## Codex mapping and Claude-specific mechanisms

| Existing mechanism | Proposed mapping / limitation |
| --- | --- |
| `CLAUDE.md` and `@file` imports | Use a short `AGENTS.md` entry point with explicit required reads and precedence. Do not assume Claude's import syntax carries over. |
| Claude agent definitions and slash commands | Translate role responsibilities into Codex-supported instructions or separate workflow nodes. `.claude/agents` does not establish a portable role-registration contract. |
| Fresh independent reviewers | Separate fresh-context sessions receiving the accepted contract, base/head SHAs, complete diff, and applicable policy. Self-review does not count as independent review. |
| Structured verdicts and evidence | Schema-backed results with logs, findings, commands, and reviewed SHA. Codex supports structured output. |
| Hooks, tool restrictions, budgets, session behavior | Verify each capability at the actual adapter boundary; similar names do not establish equivalent behavior. |
| Claude model tiers and authentication | Preserve provider identity and native authentication. Choose Codex configuration explicitly rather than assuming Claude model names, subscriptions, or budget controls translate. |

Codex supports native instruction discovery and hooks. Hook trust and coverage require explicit configuration; hooks are not a complete security boundary. See [instruction discovery](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [hooks](https://learn.chatgpt.com/docs/hooks), and [structured output](https://learn.chatgpt.com/docs/non-interactive-mode).

**Archon's inspected Codex adapter exposes fewer capabilities than Codex itself.** It supports session resume, MCP, structured output, and reasoning effort. It marks workflow hooks, agent definitions, tool restrictions, cost controls, session fork, per-node skills, and several other integrations unsupported. The inspected provider launches with `danger-full-access` and approval policy `never`; those settings do not enforce Michelle's governance. Unsupported adapter capabilities are not claims that the native Codex product lacks those features.

Reference: [current Archon adapter capabilities](https://github.com/chelleboyer/archon/blob/e237584d9c332fc492125bf9e0cb4756895f4da2/packages/providers/src/codex/capabilities.ts) and [provider implementation](https://github.com/chelleboyer/archon/blob/e237584d9c332fc492125bf9e0cb4756895f4da2/packages/providers/src/codex/provider.ts). The same relevant flags and launch settings were verified in the installed pin.

## Proposed implementation after approval

1. **Document the operating contract.** Propose a focused update to this portfolio's `AGENTS.md` and one workflow document covering roles, evidence, review rounds, stop conditions, and human authority. Preserve the portfolio brief, factual catalog, approved architecture, and static-site constraints. Define portfolio-specific protected paths rather than copying Mostly Human's application paths.
2. **Separate implementation from acceptance.** Codex implements; fresh reviewers inspect the entire change; synthesis records verified findings and coverage. Adopt the owner's test-gap severity policy explicitly. Self-review remains useful but does not replace independent review.
3. **Bind every handoff to evidence.** Record issue, branch, base/head SHAs, acceptance criteria, validation results, unavailable checks, reviewer coverage, findings, and repair count. A changed head invalidates the previous final review. Preserve reviewer and human changes.
4. **Adopt the bounded loop.** Repair → complete applicable validation → fresh full review. Stop after two repair rounds and present unresolved findings to Michelle. Carry explicit human deferrals forward without treating them as fixed. Surface scope changes for a new decision instead of expanding corrections indefinitely.
5. **Keep PR readiness distinct from approval.** Use a draft while gates remain incomplete; mark ready only after required evidence is complete. Include the eight OOUX simplicity answers for relevant UI/navigation changes and make copy changes reviewable. Michelle performs approval, merge, and release. Confirm lifecycle state from GitHub rather than inferring it from code or local success.
6. **Verify the protocol before unattended use.** Demonstrate that missing reviewers, failed validation, stale-head evidence, protected-path changes, and an attempted third repair stop handoff. Verify that approval/merge/release actions remain outside agent authority. If using Archon directly, retain its pinned consumer and address adapter gaps explicitly; do not create another scheduler or modify Archon as part of portfolio work.

### Acceptance for the adaptation

- Required context and precedence are explicit and load correctly in Codex.
- Review roles meet the explicit session-creation and packet checks above; launch evidence and required coverage are recorded. Raw-payload isolation is not claimed as verified.
- Every readiness claim identifies the exact reviewed and validated head.
- Missing evidence and exhausted repair allowance produce an honest stop.
- Human authority and deferrals remain visible at every handoff.
- No existing reviewer changes are overwritten; no requirements or tests are weakened.
- No factory runtime dependency is added to the portfolio application.
- Any mechanical enforcement not yet demonstrated is labeled procedural or unverified.

## Approval boundary

Michelle approved the plan with the required fresh-session clarification, now recorded above, and explicitly instructed that assimilation must not be implemented yet. Only this plan has been updated. Governance edits, role/hook configuration, factory integration, and Work Unit 5 remain on hold until Michelle authorizes implementation. Plan approval does not grant merge or release authority.
