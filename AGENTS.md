# AGENTS.md

## Mission

Build and maintain Michelle Builds: a living technical portfolio documenting real software systems, AI-assisted engineering, products, robotics experiments, field notes, and the evolving human + agent development process.

Before planning, implementation, or writing public portfolio copy, read:

1. `PORTFOLIO-BRIEF.md`
2. `context/MICHELLE-WORK-CATALOG.md`

## Factual source of truth

`context/MICHELLE-WORK-CATALOG.md` is the curated factual source of truth for Michelle's experience, projects, project statuses, and publication boundaries.

Do not invent accomplishments, metrics, technologies, outcomes, project statuses, or personal involvement. When the catalog does not contain a fact needed for a story, create a TODO/question for Michelle rather than filling the gap.

Respect the catalog's publication labels:

- `PUBLIC-SAFE` may be used as source material for public content, subject to review.
- `SANITIZE / ABSTRACT` must be generalized before publication.
- `CONTEXT-ONLY` must not be published without explicit human approval.

If other project documentation conflicts with an explicit status or factual correction in the work catalog, stop and surface the conflict for human review.

## Permanent rules

1. Human authority is final. Agents may analyze, plan, implement, test, review, document, and propose repairs. Agents must not merge pull requests or declare a release shipped.
2. Do not bypass failing gates, silently weaken tests, hide review findings, or rewrite requirements merely to make checks pass.
3. Never publish credentials, internal URLs, IP addresses, customer or employee information, proprietary SQL, confidential business rules, API keys, vendor secrets, or sensitive screenshots.
4. Prefer abstraction for professional systems when implementation details may belong to an employer or third party.
5. Keep the architecture simple. This is primarily a content-heavy static portfolio, not a SaaS application.
6. Prefer Markdown, static generation, minimal JavaScript, accessibility, responsive design, fast builds, and GitHub Pages compatibility unless a documented requirement justifies otherwise.
7. Do not add a framework, service, database, dependency, navigation layer, or abstraction without a concrete need.
8. Project lifecycle state must be explicit. Never infer `Shipped` because code exists.
9. Content and presentation must remain separated so new projects and Field Notes can be added without application-code changes.
10. Use real artifacts to demonstrate skills. Avoid skill meters, generic logo walls, generic AI imagery, invented metrics, and unsupported claims.
11. Distinguish Michelle's work from work performed by collaborators, vendors, or other teams.
12. Never turn a tool Michelle has experimented with into an unsupported claim of expertise.

## OOUX / ORCA gate

Before implementing the initial navigation or page-template architecture:

- identify Objects
- identify Relationships
- identify Calls to Action
- identify Attributes
- produce an object map
- propose the smallest viable information architecture

Do not implement the initial site until this architecture/design phase has been presented for human approval.

Primary candidate objects include Project, Product, Experiment, System, Field Note, Technology, Architecture, and Build Process. These are candidates, not a mandate; refine them through the ORCA analysis.

## Initial navigation hypothesis

`Home | Work | Lab | How I Build | Field Notes | About`

Treat this as a hypothesis to validate against the object model, not an immutable requirement.

## Development workflow

Idea → Brief → Planning → Issues → Implementation → Pull Request → Independent Review → Repair Loop → Human Review → Human Merge → Release

Michelle owns final review, merge, and release decisions.

## First assignment

Do not begin by building the whole site.

1. Inspect `skyejen/generalist-tech` as a reference implementation.
2. Read the complete portfolio brief.
3. Read `context/MICHELLE-WORK-CATALOG.md` and use it for factual project selection and content planning.
4. Perform OOUX/ORCA analysis.
5. Define the object model and relationships.
6. Propose the smallest viable navigation.
7. Recommend the technical architecture.
8. Define the Markdown/content schema.
9. Produce a simple wireframe/navigation model.
10. Identify the first three project case studies and any factual gaps requiring Michelle's input.
11. Break implementation into small, reviewable issues.
12. Stop for human approval.

## Design direction

Engineering notebook + modern product studio + laboratory.

Favor strong typography, whitespace, screenshots, diagrams, readable technical content, and excellent mobile behavior. Avoid corporate portfolio-template aesthetics, excessive gradients, meaningless decoration, and over-engineered navigation.
