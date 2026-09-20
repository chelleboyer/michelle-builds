# AGENTS.md

## Mission

Build and maintain Michelle Builds: a living technical portfolio documenting real software systems, AI-assisted engineering, products, robotics experiments, field notes, and the evolving human + agent development process.

Read `PORTFOLIO-BRIEF.md` before planning or implementation.

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
3. Perform OOUX/ORCA analysis.
4. Define the object model and relationships.
5. Propose the smallest viable navigation.
6. Recommend the technical architecture.
7. Define the Markdown/content schema.
8. Produce a simple wireframe/navigation model.
9. Identify the first three project case studies.
10. Break implementation into small, reviewable issues.
11. Stop for human approval.

## Design direction

Engineering notebook + modern product studio + laboratory.

Favor strong typography, whitespace, screenshots, diagrams, readable technical content, and excellent mobile behavior. Avoid corporate portfolio-template aesthetics, excessive gradients, meaningless decoration, and over-engineered navigation.
