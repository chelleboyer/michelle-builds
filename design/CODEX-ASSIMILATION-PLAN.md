# Codex factory-protocol assimilation plan

**Status:** Proposed — awaiting Michelle's approval.  
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

This was a read-only inspection, not a live verification of factory execution or provider integration. No factory workflow was launched. Historical installation notes in `FACTORY.md` coexist with later run records; they should not all be treated as current state.

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

Reviewers inspect the actual diff, relevant consumers, requirements, and architecture. The implementation report is supporting evidence, not the review's scope. Missing reports from required reviewers block readiness.

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
- Review roles are independent and their required coverage is recorded.
- Every readiness claim identifies the exact reviewed and validated head.
- Missing evidence and exhausted repair allowance produce an honest stop.
- Human authority and deferrals remain visible at every handoff.
- No existing reviewer changes are overwritten; no requirements or tests are weakened.
- No factory runtime dependency is added to the portfolio application.
- Any mechanical enforcement not yet demonstrated is labeled procedural or unverified.

## Approval boundary

This document is the reviewable proposal. Michelle's approval is required before editing governance, configuring roles/hooks, integrating factory execution, or resuming Work Unit 5 under the proposed protocol. Approval of the plan does not grant merge or release authority.
