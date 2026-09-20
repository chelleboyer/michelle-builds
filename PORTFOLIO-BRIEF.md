# Michelle Builds — Portfolio Project Brief

## Purpose

Build a public technical portfolio documenting Michelle Boyer’s evolution from experienced full-stack developer to development manager, AI-augmented builder, product creator, and robotics experimenter.

This is not a traditional résumé website. It should feel like a living technical field journal: part portfolio, part engineering notebook, part laboratory.

The portfolio itself should be built using the disciplined agent-assisted development process it documents.

## Positioning

# Michelle Boyer

**Developer → Manager → AI-Augmented Builder**

Supporting line:

> Things I build, systems I run, experiments I probably shouldn't have started at 5 AM.

The tone should be technically credible without becoming corporate or overly polished. Personality should come from the work.

Avoid résumé-template aesthetics, generic AI imagery, excessive gradients, meaningless skill meters, “AI visionary” language, marketing buzzwords, and giant walls of technology logos.

Prefer strong typography, screenshots, diagrams, architecture, code snippets, experiment results, short technical explanations, and links to real projects where appropriate.

## Audience

The site should work for technical peers, employers/professional contacts, builders interested in practical AI-assisted engineering, and as a durable record for Michelle herself.

A professional visitor should be able to understand Michelle’s technical depth and leadership experience within approximately two minutes.

## OOUX / ORCA

Use OOUX/ORCA principles before designing final navigation. Do not begin by inventing pages.

Candidate primary objects:

- Project
- Product
- Experiment
- System
- Field Note
- Technology
- Architecture
- Build Process

Determine their Attributes, Relationships, and Calls to Action before implementation.

Example: Microduck RL may relate to Robotics → Reinforcement Learning → Microduck → Training Experiments → Hugging Face → Duck Factory telemetry. Users should move naturally between related objects without an unnecessarily deep menu hierarchy.

## Navigation hypothesis

Keep top-level navigation intentionally small. Starting hypothesis:

**Home | Work | Lab | How I Build | Field Notes | About**

The ORCA analysis may refine this.

## Home

Answer quickly:

1. Who is Michelle?
2. What does she build?
3. What is interesting here?

Include a short introduction, selected work, current experiments, latest Field Notes, a How I Build teaser, GitHub, and résumé/about access. Do not overload the page.

## Work

Substantial professional engineering work may include anonymized case studies involving central price-book/orchestration systems, POS/data platforms, merchandise ordering, fleet settlement, scan data, job management, workflow engines, sales-performance reporting, early-sales reporting, and fuel-pricing systems.

Do not expose proprietary or employer-confidential details.

Case-study structure:

- Problem
- Context
- Architecture
- Decisions
- Result
- Lessons

## Lab

Experimental work may include:

### Microduck RL
Reinforcement-learning experiments for physical Microduck behaviors such as hopping, hopscotch, ball walking, kicking, balancing, and locomotion.

### Duck Factory
Telemetry, observability, and insight tooling supporting Microduck training. Keep this explicitly distinct from `microduck_rl`, where actual training runs occur.

### Pizza Vision
Computer-vision experiments including local inference and RF-DETR work.

### Reachy Mini
Human/robot interaction experiments.

### AI Software Factory Experiments
Archon, PIV loops, coding agents, model routing, automated implementation, review agents, mutation testing, agent cost, human approval gates, and OOUX integration.

Experiments do not need to succeed. Failures are useful artifacts.

## Products

Products can initially live within Work or Lab instead of requiring another top-level navigation item.

### Mostly Human
A small product studio exploring software based on ordinary human problems rather than technology looking for a problem.

- **Before I Forget** — status: Ideation
- **I Did a Thing** — status: In Development

Do not present concepts as shipped products.

### Safety Claws
Passive software-safety tooling built around the philosophy:

**Observe. Detect. Explain. Don't silently change things.**

Potential subjects include import safety analysis, CSV structural-change detection, migration analysis, configuration drift detection, and schema-change monitoring.

## How I Build

This should become a signature section.

Document the evolving workflow:

`Idea → Brief → Factory Planning → Issues → Agent Implementation → Pull Request → Independent Review → Repair Loop → Human Review → Human Merge → Release`

The human remains the authority at important control boundaries. Agents do not merge production changes; Michelle performs the merge.

Potential topics:

- agent specialization
- context management
- review independence
- mutation testing
- test gates
- Git safety
- cost control
- model selection
- issue and PR sizing
- repair loops
- human approval
- avoiding review churn
- Archon lessons
- PIV loop integration
- OOUX/ORCA design integration

Do not pretend the methodology is finished. The experimentation is part of the story.

## Factory architecture

Initial conceptual flow:

```text
                  HUMAN
                    │
                  IDEA
                    │
                  BRIEF
                    │
             FACTORY PLANNER
                    │
               WORK ISSUES
                    │
          ┌─────────┼─────────┐
          │         │         │
       AGENT     AGENT     AGENT
          │         │         │
          └─────────┼─────────┘
                    │
                   PR
                    │
              REVIEW AGENT
                    │
             ┌──────┴──────┐
             │             │
           PASS          REPAIR
             │             │
             │        IMPLEMENTER
             │             │
             └─────── REVIEW
                    │
                 HUMAN
                    │
                  MERGE
                    │
                 RELEASE
```

Eventually replace this with a clean responsive diagram.

## Field Notes

Support easy Markdown-based short-form technical writing. Publishing a note should not require modifying application code.

Potential topics include model-usage burn, independent review, human-owned merges, teaching a factory OOUX, mutation testing AI-generated applications, running an AI development environment from an iPhone, training Microduck without a local GPU, factory failures, surprising agent strengths/weaknesses, autonomy boundaries, complexity creep, and what experienced developers notice when vibe coding.

## Project lifecycle

Support explicit states such as:

- Ideation
- Prototype
- Experiment
- In Development
- Testing
- Shipped
- Paused
- Archived

Never infer that something shipped merely because code exists.

## Project metadata

Structured content should be able to support fields such as:

```yaml
title:
slug:
summary:
status:
category:
started:
updated:
technologies:
repository:
demo:
featured:
related_projects:
tags:
```

Future filtering should be possible without requiring it in the first release.

## Technology and skills

Demonstrate skills primarily through projects rather than a giant logo wall.

Relevant areas include C#, .NET, ASP.NET Core, MVC, Razor, JavaScript, REST APIs, EF Core, SQL Server, SQL, SSIS, ETL, data warehousing, reporting, data modeling, Azure, Azure VMs, IIS, Linux, VPS environments, GitHub, CI/CD, Claude Code, OpenAI models, agents, Archon, PIV workflows, RAG, evaluation, model orchestration, Python, MuJoCo, reinforcement learning, Hugging Face, Weights & Biases, Roboflow, RF-DETR, and computer vision.

## About

Keep the biography relatively short. Tell the progression:

**Developer → Technical Lead/Manager → AI-Augmented Builder**

Emphasize substantial software-engineering experience combined with current experimentation in AI engineering, agentic development, and robotics. Link to a downloadable résumé when available.

## Visual direction

**Engineering notebook + modern product studio + laboratory.**

Favor excellent typography, generous whitespace, restrained color, screenshots, diagrams, cards only where objects genuinely behave like cards, readable technical content, and excellent mobile behavior.

Dark mode is desirable but must not delay the initial release.

## Technical direction

Use `skyejen/generalist-tech` as inspiration, not something to clone blindly.

Prefer a static-content architecture with Markdown, Git, GitHub Pages compatibility, fast builds, minimal JavaScript, responsive/accessibile output, SEO/OpenGraph metadata, sitemap, syntax highlighting, diagram support, and easy creation of projects and Field Notes.

MkDocs Material is a strong initial candidate. Do not introduce a JavaScript application framework without a demonstrated requirement.

## Content architecture hypothesis

```text
docs/
  index.md
  work/
  lab/
  products/
  projects/
  how-i-build/
  notes/
  about/
assets/
  images/
  diagrams/
```

The factory may refine this after ORCA analysis.

## Privacy and safety

Before publishing professional content, evaluate it for credentials, internal URLs, IP addresses, customer information, employee information, proprietary SQL, confidential business rules, internal architecture details, vendor secrets, API keys, and sensitive screenshots.

When uncertain, abstract the implementation.

## MVP

Do not document everything before launching.

Version 1 needs Home, About, Work index, Lab index, How I Build, Field Notes, three strong project pages, one factory workflow diagram, GitHub linking, and responsive design.

Suggested first case studies:

1. Mostly Human Factory
2. Microduck RL
3. One anonymized production-system case study

Together these demonstrate product thinking, experimental engineering, and professional engineering.

## Factory rules

Agents may analyze, plan, create issues, implement, test, review, propose repairs, and document.

Agents may not merge PRs, bypass failing gates, silently weaken tests, hide unresolved review findings, publish sensitive information, or declare work shipped without evidence.

Michelle owns final review, merge, and release decisions.

## Success criterion

A visitor should leave understanding that Michelle builds real software systems, experiments aggressively with emerging technology, and is developing a disciplined way for humans and AI agents to build software together.

The site should prove this through artifacts rather than simply claiming it.

## First Codex assignment

Do not implement the site yet.

1. Inspect `skyejen/generalist-tech` as a reference repository.
2. Read this brief and `AGENTS.md` in full.
3. Perform OOUX/ORCA analysis.
4. Define the portfolio object model and relationships.
5. Propose the smallest viable information architecture and navigation.
6. Recommend the technical architecture.
7. Define the Markdown/content schema.
8. Produce a simple wireframe/navigation model.
9. Identify the first three case studies and what source material is still needed for each.
10. Break implementation into small reviewable issues.
11. Stop and present the architecture/design package for human approval before implementation.

The goal is not to create a fancy portfolio. The goal is a durable, low-maintenance technical record of things built, things learned, things attempted, and the evolving process behind them.
