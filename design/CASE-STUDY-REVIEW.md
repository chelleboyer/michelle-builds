# Initial case-study editorial review

Work unit 3 of the [architecture](ARCHITECTURE-ORCA.md): three case-study
skeletons grounded in the curated catalog. These are editorial drafts, not final
public pages. They live outside `docs/` under the
[content guide's draft rules](CONTENT-GUIDE.md#draft-review-then-include-in-the-site).

The package is ready for factual/editorial review. Publication remains pending
answers and artifact review; a successful build does not resolve factual gaps.

## Drafts and proposed placement

| Draft | Intended public destination | State of the draft |
| --- | --- | --- |
| [Mostly Human factory](../drafts/case-studies/mostly-human-factory.md) | `docs/lab/mostly-human-factory.md` | Supported process and OOUX lesson; concrete run/artifact and tradeoff still needed |
| [Microduck RL](../drafts/case-studies/microduck-rl.md) | `docs/lab/microduck-rl.md` | Training/telemetry boundary established; contribution detail, outcome, and lesson still needed |
| [Distributed retail processing](../drafts/case-studies/distributed-retail-processing.md) | `docs/work/distributed-retail-processing.md` | Generalized architecture established; lifecycle, detailed contribution, decision, and lesson still needed |

Microduck RL and Duck Factory are presented together in one initial story, as the
approved case-study selection proposes. This does not merge their responsibilities
or imply Duck Factory launches training. A separate Duck Factory page can follow
when enough reviewed material exists. No duplicate page or invented relationship
link is needed now.

## Factual basis and limits

All factual assertions come from `context/MICHELLE-WORK-CATALOG.md` and the brief.
The drafts do not use repository activity as evidence of deployment, training
success, or individual authorship. Editorial questions are TODOs, not assertions.

| Draft / claim group | Catalog source | Treatment |
| --- | --- | --- |
| Factory purpose and product context | Mostly Human; I Did a Thing; Before I Forget | PUBLIC-SAFE; preserve In Development and Ideation separately from the factory's Experiment state |
| Factory process, gates, roles, ongoing topics | Mostly Human factory / agentic engineering | PUBLIC-SAFE; process experimentation, not measured effectiveness or a completed methodology |
| OOUX observation and response | OOUX / ORCA | PUBLIC-SAFE; UX complexity observation and incorporation of object modeling; no claim of measured improvement |
| Intended workflow sequence | Brief: How I Build; catalog: factory and OOUX sections | Explicitly presented as intended process, not an audit of every run |
| Microduck goals and compute constraint | Microduck robotics / microduck_rl | PUBLIC-SAFE; goals remain goals; Experiment reflects the catalog's explicit description of experiments |
| Duck Factory responsibility | Microduck robotics / Duck Factory | PUBLIC-SAFE; telemetry/insight/observability only; does not perform or launch training |
| Interactive robot concept | Microduck robotics / Interactive Microduck concept | Ideation only; no implemented interaction claim |
| Retail architecture and contribution | Professional engineering systems / Central Price Book / distributed store processing | SANITIZE / ABSTRACT; generalized location-specific work, claims, central tracking, duplicate prevention, and troubleshooting |
| Retail lifecycle and outcomes | Not established for this system | Explicit TODOs; do not borrow Daily Performance or Early Sales statuses |

Technology lists remain narrow: Archon is explicitly tied to factory work. The
catalog's general professional and experimental technology lists are not enough
to attribute a specific stack to either of the other case studies. Public repo
URLs, dates, demos, and metrics are omitted until verified and approved.

## Questions for Michelle

Answer only with information safe to commit to this repository. Generalized
examples are sufficient; no private infrastructure or operational data is needed.

### Mostly Human factory

1. Which concrete run or product change best demonstrates the factory? What did
   you do, what did agents do, and what changed after review or repair?
2. What was one real tradeoff or lesson? An OOUX before/after example would support
   the existing lesson without requiring a claim about overall productivity.
3. Is there an approved public PR, diagram, or sanitized artifact we may use?

### Microduck RL and Duck Factory

1. Which behavior attempt should anchor the story? Was the result in simulation,
   on physical hardware, incomplete, or unsuccessful? What was actually observed?
2. Which parts did you build or adapt, and which require upstream/collaborator credit?
3. What stack and telemetry path are accurate for that attempt, and which artifact
   can be shared? What did you learn from the attempt?

### Distributed retail processing

1. What is this system's current lifecycle state, and which part of it is the story about?
2. What did you personally design, implement, or operate, versus other contributors?
3. What is one safe-to-describe decision, alternative, outcome, or failure lesson?
4. May we use a generalized diagram of the listed responsibilities? Which details
   should stay abstract even if they are technically relevant?

## Before moving a draft into public content

- Resolve required lifecycle, contribution, decision, result, and lesson gaps; remove
  every TODO and editorial/source discussion from the public copy.
- Check any new factual statements against Michelle's answers and update the catalog
  with confirmed corrections where needed. Surface contradictions rather than silently
  selecting one version.
- Review proposed artifacts for publication rights, confidentiality, and attribution.
  No artifacts are included or manufactured in these drafts.
- Keep one canonical page per story and use relative links to real pages. Add the
  reviewed pages to Work/Lab indexes and curate Home links at that time.
- Run a strict build, review rendered content, and submit public-content changes for
  Michelle's editorial/merge decision. Deployment remains a separate human action.

## Deliberate limits

No new public pages, navigation links to drafts, frameworks, dependencies, runtime
code, diagrams purporting to show an unverified implementation, or deployment
changes. Templates are used for structure; missing evidence is left visible to the
reviewer. These skeletons do not yet satisfy the brief's launch requirement for
three strong, artifact-backed project pages.
