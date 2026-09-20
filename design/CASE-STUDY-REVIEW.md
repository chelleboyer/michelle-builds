# Initial case-study editorial review

Work unit 3 of the [architecture](ARCHITECTURE-ORCA.md): three case-study skeletons grounded in reviewed project context. These remain editorial drafts outside `docs/`; publication still requires Michelle's editorial approval and artifact review.

## Drafts and proposed placement

| Draft | Intended public destination | State of the draft |
| --- | --- | --- |
| [Mostly Human factory](../drafts/case-studies/mostly-human-factory.md) | `docs/lab/mostly-human-factory.md` | Concrete repair-loop lesson and OOUX lesson now documented; public artifact still needs selection/review |
| [Microduck training lab](../drafts/case-studies/microduck-rl.md) | `docs/lab/microduck-rl.md` | Updated for the new `chelleboyer/microduck-lab` fork and lab → graduation → observability boundaries; concrete run artifact still needed |
| [Distributed retail processing](../drafts/case-studies/distributed-retail-processing.md) | `docs/work/distributed-retail-processing.md` | Generalized architecture established; lifecycle, detailed contribution, decision, and lesson still require Michelle |

## Resolved during independent review

### Mostly Human factory

A concrete process failure is now part of the draft. A repair stage addressed its known findings, but a subsequent broader review surfaced additional concerns including ordering, identity/email normalization, password length, and factory-level review behavior. The supported lesson is intentionally narrow: **repairing known findings is not a substitute for a fresh complete review of the repaired change**.

The OOUX lesson remains separate: observed navigation/UI complexity in a simple product led to adding object modeling before screen/navigation generation. Neither example is presented as measured productivity or quality improvement.

### Microduck

The architecture changed with the new public working fork `chelleboyer/microduck-lab`. The draft now treats:

- `chelleboyer/microduck-lab` as the fast behavior experimentation environment;
- `microduck_rl` as the graduation target for promising behaviors and the path toward higher-fidelity/sim-to-real work;
- Duck Factory as telemetry/insight/observability only, never the training launcher;
- Archon as engineering-workflow orchestration, not robot runtime.

The working lab uses MuJoCo with Stable-Baselines3/PPO and is designed for CPU-friendly Linux/VPS experimentation. Upstream Microduck Lab work must remain credited. No target behavior is described as successfully transferred to physical hardware.

## Remaining questions for Michelle

Only genuinely unresolved facts should block this editorial package.

### Mostly Human factory

1. Which public PR/review trail should be used as the artifact for the repair-loop story, or should the case study use a sanitized diagram/excerpt instead?

### Microduck

1. Which actual training run should become the artifact-backed example once one is ready? A failed or incomplete run is acceptable; we need the observed result, not a success story.
2. Is there any additional upstream/collaborator credit beyond the upstream Microduck Lab project that should appear in the public case study?

### Distributed retail processing

1. What is this system's current lifecycle state, and which portion of the architecture should the story center on?
2. What did Michelle personally design, implement, or operate versus collaborators/other teams?
3. What is one safe-to-describe design decision, alternative, outcome, or failure lesson?
4. May the public page include a generalized architecture diagram? Which details should remain abstract even in that diagram?

## Before moving drafts into public content

- Resolve the remaining lifecycle/contribution/evidence gaps and remove every TODO/editorial note from public copy.
- Review artifacts for publication rights, confidentiality, and attribution.
- Keep one canonical page per story and link only to real public resources.
- Run a strict build and rendered-content review before Michelle's merge decision.
- Deployment remains a separate human action.

## Deliberate limits

No new public pages, navigation links to drafts, frameworks, dependencies, runtime code, unverified diagrams, or deployment changes are part of this editorial package. The drafts remain evidence-constrained: missing evidence stays missing rather than being converted into a plausible story.
