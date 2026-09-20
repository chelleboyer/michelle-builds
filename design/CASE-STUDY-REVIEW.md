# Initial case-study editorial review

Work unit 3 of the [architecture](ARCHITECTURE-ORCA.md): three case-study skeletons grounded in reviewed project context. These remain editorial drafts outside `docs/`; publication still requires Michelle's final editorial approval and artifact review.

## Drafts and proposed placement

| Draft | Intended public destination | State of the draft |
| --- | --- | --- |
| [Mostly Human factory](../drafts/case-studies/mostly-human-factory.md) | `docs/lab/mostly-human-factory.md` | Repair-loop and OOUX lessons documented; real public PR/review trail approved as evidence |
| [Microduck training lab](../drafts/case-studies/microduck-rl.md) | `docs/lab/microduck-rl.md` | Working lab repo approved as current artifact; training-run evidence will be added later when an actual run is ready |
| [Distributed retail processing](../drafts/case-studies/distributed-retail-processing.md) | `docs/work/distributed-retail-processing.md` | Lifecycle, contribution boundary, architectural driver, tested boundary, next milestone, and diagram permission confirmed |

## Resolved during independent review and human interview

### Mostly Human factory

A repair stage addressed its known findings, but a subsequent broader review surfaced additional concerns including ordering, identity/email normalization, password length, and factory-level review behavior. The supported lesson is intentionally narrow: **repairing known findings is not a substitute for a fresh complete review of the repaired change**.

The OOUX lesson remains separate: observed navigation/UI complexity in a simple product led to adding object modeling before screen/navigation generation. The unsupported cost comparison was removed; the design gate is described only as intended to avoid later navigation rework.

Michelle approved using the real public PR/review history as the evidence artifact, with summarization/sanitization where appropriate.

### Microduck

The current architecture treats:

- `chelleboyer/microduck-lab` as the fast behavior experimentation environment;
- `microduck_rl` as the graduation target for promising behaviors and the path toward higher-fidelity/sim-to-real work;
- Duck Factory as telemetry/insight/observability only, never the training launcher;
- Archon as engineering-workflow orchestration, not robot runtime.

The working lab uses MuJoCo with Stable-Baselines3/PPO and is designed for CPU-friendly Linux/VPS experimentation. Michelle confirmed that the upstream Microduck Lab project should be credited and Pollen Robotics should be credited for Microduck where appropriate. No additional individual collaborator credit is currently required.

Michelle approved the public `chelleboyer/microduck-lab` repository as the current artifact. A real training run—successful, failed, or incomplete—can be added later with its observed result. No target behavior is described as successfully transferred to physical hardware.

### Distributed retail processing

Michelle confirmed the system is **in development / integration**. The tested execution boundary can terminate/configure/launch the existing location-side application for a target location, generate its price-book output, and repeat through locations in a loop.

The VM Manager is Michelle's orchestration design and is the next major test boundary after the worker VM specification is finalized. It is not yet described as proven.

The architectural driver is also confirmed: a required vendor-side change could not move at the speed the business needed, so the solution centralizes the existing location workflow rather than waiting for or rewriting the vendor process. A fleet of VMs reproduces centrally what a store would already do.

Michelle's contribution includes the distributed architecture, central job/history model, worker-claiming and duplicate-prevention concepts, VM-manager/orchestration design, and hands-on work/testing around the application automation. Adjacent ETL/data-loading/downstream work has other contributors and must not be presented as Michelle's sole implementation.

Michelle approved a sanitized public architecture diagram using this shape:

**Central Job Queue / History → VM Manager → Fleet of Worker VMs → Existing Location Application → Store-equivalent Price Book Output**

Employer/vendor identity, counts, internal service/table names, schedules, credentials, infrastructure identifiers, and proprietary formats remain excluded.

## Remaining evidence work

No factual interview question currently blocks this draft package. Before promotion to public content:

- Select the specific public Mostly Human PR/review trail and review its presentation.
- For Microduck, use the working lab repo now; add a training-run artifact only when an actual run is ready and reviewed.
- Create only the approved generalized retail architecture diagram; do not reconstruct confidential implementation details.
- Synchronize these confirmed facts into the curated work catalog so future agents do not have to infer them from draft prose.
- Run a strict build and rendered-content review before Michelle's merge decision.
- Deployment remains a separate human action.

## Deliberate limits

No new public pages, navigation links to drafts, frameworks, dependencies, runtime code, unverified diagrams, or deployment changes are part of this editorial package. The drafts remain evidence-constrained: missing evidence stays missing rather than being converted into a plausible story.
