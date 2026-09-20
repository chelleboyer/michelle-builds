# Michelle Builds — ORCA & Architecture Proposal

Status: **Proposed for human review**

This document is the design gate before implementation. It intentionally keeps the portfolio simpler than the initial list of possible objects/pages.

## 1. Design principle

The portfolio is fundamentally a collection of **things Michelle built or learned**, connected by a small number of meaningful relationships. Visitors should not need to understand Michelle's internal taxonomy before finding interesting work.

The site should optimize for:

1. understanding Michelle quickly;
2. seeing credible artifacts/work;
3. moving from one interesting thing to related things;
4. understanding how she builds with agents;
5. reading short field notes without navigating a documentation maze.

## 2. ORCA — core objects

### Object A: Project

The primary object. A Project represents a substantial thing Michelle built, designed, experimented with, or materially contributed to.

**Attributes**

- title
- short summary
- lifecycle status
- kind: professional / product / experiment
- date or date range where appropriate
- technologies
- Michelle's role/contribution
- publication classification
- problem/context
- architecture/approach
- decisions/tradeoffs
- result/current state
- lessons
- repository/demo when public
- related projects
- related field notes

**Relationships**

- Project uses Technologies
- Project has Field Notes
- Project relates to other Projects
- Project may demonstrate a Build Practice

**Calls to action**

- Read case study
- View public repository/demo when available
- Read related Field Notes
- Explore related Project

### Object B: Field Note

A short observation, lesson, failure, decision, or experiment log. Field Notes should be cheap to publish.

**Attributes**

- title
- date
- summary
- body
- tags/topics
- related project(s)
- optional external references

**Relationships**

- Field Note may belong to one or more Projects
- Field Note may discuss a Build Practice or Technology

**Calls to action**

- Read note
- Open related project
- Follow external reference when useful

### Object C: Build Practice

A durable explanation of how Michelle works with agents and software-development controls. This powers the signature **How I Build** section.

Examples include human merge authority, independent review, repair loops, mutation testing, OOUX/ORCA before UI generation, Git safety, context management, and model/cost decisions.

**Attributes**

- name
- problem it addresses
- practice
- rationale
- examples/evidence
- current maturity
- related Field Notes

**Relationships**

- Build Practice appears in Projects
- Build Practice has supporting Field Notes

**Calls to action**

- Understand the practice
- See it used in a project
- Read lessons/notes

## 3. Objects deliberately NOT promoted to first-class navigation

The initial brief listed Product, Experiment, System, Technology, and Architecture as candidate objects. For MVP, they do not need independent top-level object systems.

- **Product / Experiment / Professional System** become `kind` or presentation categories of Project.
- **Technology** is metadata attached to Projects and Notes; no technology encyclopedia is needed.
- **Architecture** belongs inside Project case studies unless a specific architecture later earns its own reusable article.

This reduction is intentional. It prevents taxonomy from becoming the product.

## 4. Information architecture

Recommended top navigation:

**Work | Lab | How I Build | Field Notes | About**

The site logo/name returns Home, so a separate Home navigation item is unnecessary on desktop if usability remains clear.

### Home

Purpose: rapid orientation and curated entry points.

Sections:

1. concise hero / positioning
2. Featured Work
3. From the Lab
4. How I Build teaser
5. Recent Field Notes
6. About/GitHub/resume links

### Work

Professional and substantial product/software case studies. This is not a chronological résumé.

### Lab

Experiments, robotics, AI factory work, computer vision, prototypes, and unfinished-but-interesting work.

### How I Build

The human + agent engineering process and its evolving practices.

### Field Notes

Chronological short-form writing, filterable later if volume requires it.

### About

Short professional narrative, skills grounded in projects, and resume/contact links.

## 5. Project classification

Use one Project content model with a `kind` attribute rather than separate content engines.

Suggested values:

- `professional`
- `product`
- `experiment`

A project can appear in Work or Lab based on kind/status/editorial choice without duplicating content.

## 6. Lifecycle status

Use explicit values only:

- Ideation
- Prototype
- Experiment
- In Development
- Testing
- Shipped
- Paused
- Archived
- Completed / Deployed when professional context requires that distinction

Never derive status from repository activity.

## 7. Content schema proposal

Project front matter:

```yaml
title:
slug:
summary:
kind:
status:
started:
updated:
featured: false
technologies: []
repository:
demo:
related_projects: []
related_notes: []
tags: []
```

Field Note front matter:

```yaml
title:
slug:
date:
summary:
related_projects: []
tags: []
```

Build Practice front matter:

```yaml
title:
slug:
summary:
maturity:
related_projects: []
related_notes: []
```

Publication classification is intentionally not exposed in public front matter unless the implementation can guarantee it never renders. Sensitive/source-only material should remain in the repository's context area, not copied into public content merely with a hidden flag.

## 8. Technical architecture recommendation

Use **MkDocs + Material for MkDocs** for MVP unless implementation testing exposes a concrete blocker.

Reasons:

- Markdown-first
- static output
- low operational burden
- GitHub Pages friendly
- strong technical-writing ergonomics
- syntax highlighting
- navigation/search support
- extensibility without requiring a SPA
- matches the field-journal/documentation nature of the portfolio

Avoid a database, API backend, authentication, CMS, React/Next application, or client-side state framework for MVP.

Suggested capabilities:

- Material for MkDocs
- Mermaid support for architecture/process diagrams
- Markdown extensions for callouts/code
- small custom CSS for identity beyond stock documentation appearance
- GitHub Actions deployment to Pages
- metadata/SEO/OpenGraph support where practical

## 9. Repository structure

```text
AGENTS.md
PORTFOLIO-BRIEF.md
context/
  MICHELLE-WORK-CATALOG.md
design/
  ARCHITECTURE-ORCA.md
mkdocs.yml
docs/
  index.md
  work/
    index.md
    <project>.md
  lab/
    index.md
    <project>.md
  how-i-build/
    index.md
    <practice>.md
  notes/
    index.md
    <note>.md
  about/
    index.md
  assets/
    images/
    stylesheets/
```

For MVP, do not create elaborate generator code merely to normalize front matter. Start with conventional Markdown pages and add automation only after repetition demonstrates a need.

## 10. Wireframe

### Home

```text
┌───────────────────────────────────────────────────────────┐
│ MICHELLE BUILDS       Work Lab How I Build Notes About    │
├───────────────────────────────────────────────────────────┤
│                                                           │
│ Michelle Boyer                                            │
│ Developer → Manager → AI-Augmented Builder                │
│                                                           │
│ Things I build, systems I run, experiments I probably     │
│ shouldn't have started at 5 AM.                           │
│                                                           │
├───────────────────────────────────────────────────────────┤
│ FEATURED WORK                                             │
│ [case study]      [case study]                            │
├───────────────────────────────────────────────────────────┤
│ FROM THE LAB                                              │
│ [Mostly Human]    [Microduck]                             │
├───────────────────────────────────────────────────────────┤
│ HOW I BUILD                                               │
│ Idea → Brief → Agents → Review → Human Merge              │
│ [See the process]                                         │
├───────────────────────────────────────────────────────────┤
│ RECENT FIELD NOTES                                        │
│ note                         date                          │
│ note                         date                          │
├───────────────────────────────────────────────────────────┤
│ About / GitHub / Resume                                   │
└───────────────────────────────────────────────────────────┘
```

### Project

```text
TITLE                                      [STATUS]
One-sentence summary

Role / Kind / Technologies / Links

Problem
Context
Architecture / Approach
Decisions & Tradeoffs
Result / Current State
Lessons

Related Notes
Related Projects
```

### How I Build

```text
HOW I BUILD
Short explanation: evolving practice, not doctrine

[workflow diagram]

Practices
- Human owns merge
- Independent review
- Repair loops
- OOUX before screens
- Testing / mutation testing
- Git safety
- Context & model decisions

Field notes from the experiment
```

## 11. Initial case studies

### 1. Mostly Human / agentic software factory

Why first: strongest bridge between software engineering, product development, agent orchestration, human control, and current experimentation.

Known facts are sufficient for an initial case-study skeleton. Human input will be needed before publishing strong claims about measurable results or efficiency.

### 2. Microduck RL + Duck Factory

Present as a related pair while maintaining the factual boundary:

- `microduck_rl` = actual training workspace
- Duck Factory = telemetry/observability/insight tooling

Do not claim behaviors are successfully trained without evidence.

### 3. Distributed retail processing architecture — anonymized

Create a professional case study from the generalized Central Price Book/distributed processing experience. Focus on queueing, distributed workers, atomic claims, idempotency, failure handling, and observability.

Do not publish employer name, store count, service names, internal table names, infrastructure identifiers, vendor details, or proprietary file formats.

## 12. Initial Field Notes

Good early notes:

- Why the human still owns merge
- Teaching a software factory OOUX
- What mutation testing exposed in agent-generated code
- Building from an iPhone and a VPS
- When agent autonomy creates review churn

These should be concise and evidence-based. If details are not in the factual catalog, leave a TODO rather than inventing a story.

## 13. Implementation work units after approval

### Issue 1 — Static site foundation

Set up MkDocs Material, base configuration, navigation shell, custom CSS entry point, local build instructions, and basic GitHub Pages workflow.

### Issue 2 — Core page templates/content conventions

Implement Home, Work, Lab, How I Build, Field Notes, About, and reusable Markdown conventions without introducing a custom application framework.

### Issue 3 — First project case-study content

Add reviewed/sanitized skeletons for Mostly Human, Microduck/Duck Factory, and the anonymized distributed-processing case study.

### Issue 4 — How I Build workflow

Add the process diagram and initial practice pages using the factual catalog and approved language.

### Issue 5 — Visual polish and responsive review

Make the site feel like an engineering notebook/product lab rather than stock MkDocs. Validate mobile layout, accessibility basics, link integrity, and content readability.

### Issue 6 — Deployment and release validation

Validate clean build, GitHub Pages deployment, metadata, sitemap, links, and release checklist. Human decides whether to publish.

## 14. Deliberate non-goals for MVP

- CMS
- database
- authentication
- comments
- analytics dashboard
- dynamic filtering UI
- JavaScript application framework
- automated résumé generation
- skill scores
- technology encyclopedia
- complex taxonomy
- automatic publishing from private context files
- AI chatbot on the portfolio

## 15. Questions for Michelle before public content is finalized

1. Which public contact methods should appear: GitHub, LinkedIn, email, other?
2. Should Road Ranger/employer identity be named publicly, or should all professional case studies remain employer-neutral?
3. Which public repositories should be linked for Mostly Human, Microduck, Duck Factory, Safety Claws, or other work?
4. Is a résumé ready to publish, and should it be downloadable from the site?
5. For the anonymized professional case study, are there any additional architecture details Michelle explicitly considers safe to publish?
6. Does Michelle want a photo/avatar, or should the site remain artifact-first with no portrait?

## 16. Approval gate

No production-site implementation should begin until Michelle reviews this proposal. The main decision is whether this intentionally reduced object model and navigation accurately reflect how she wants visitors to experience the work.
