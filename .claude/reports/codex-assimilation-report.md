# Codex assimilation implementation report

Plan: `design/CODEX-ASSIMILATION-PLAN.md`, including the approved fresh-session clarification.
Branch: `docs/codex-assimilation-plan`.

## Implementation

- Updated AGENTS.md to load the operating protocol, preserve existing factual and architecture authority, and make human-only approval/merge/release explicit.
- Added `design/CODEX-WORKFLOW.md` with roles, independent-session creation, allowed context, evidence, repair limits, protected paths, and procedural versus mechanical limits.
- Added a standard-library-only evidence checker and packet template. It prepares exact fresh launch arguments and checks recorded handoff evidence; it does not dispatch agents or change GitHub state.
- Added 20 regression tests with real scratch Git repositories, reports, and CLI exit checks.
- Linked contributor validation and protocol instructions from README.

## Validation before independent review

- `python3 -m unittest discover -s tests/protocol -v`: 20 passing tests.
- `python -m pip check`: no broken requirements.
- `python -m mkdocs build --strict`: passed. Existing informational notices about three deliberately linked practice pages remain.
- `git diff --check`: passed.

Independent review, any repair results, exact head evidence, and CI status are recorded on the PR. This implementation report is not independent-review evidence and is excluded from specialist packets.

## Scope and limitations

No approved-plan changes or new architecture decisions. The approved plan remains a historical approval artifact; the task's later explicit implementation authorization is recorded in the operating protocol.

Work Unit 5 remains paused and its original workspace changes are preserved. No public site content, runtime dependencies, deployment workflow, Archon installation, or external reference repository changed. No hook, scheduler, or unattended automation was installed.

The checker cannot attest to human identity, truthful records, or the host's internal model payload. Fresh-session creation uses the approved explicit tool contract. Shared filesystem access and the inconclusive inherited-context probe remain disclosed. No approval, merge, release, or deployment is authorized by a passing result.
