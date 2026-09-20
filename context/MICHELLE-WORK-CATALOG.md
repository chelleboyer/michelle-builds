# Michelle Work Catalog

## Purpose

This file is curated factual context for coding and content agents working on Michelle Builds. Use it to understand Michelle's body of work without inventing accomplishments, statuses, metrics, technologies, or outcomes.

This is not automatically public copy.

## Publication labels

- **PUBLIC-SAFE** — suitable as source material for public portfolio content, subject to normal editorial review.
- **SANITIZE / ABSTRACT** — useful portfolio material, but employer, vendor, customer, architecture, operational, or implementation details must be generalized before publication.
- **CONTEXT-ONLY** — helps understand Michelle's experience or current work but should not be published unless Michelle explicitly approves it.

When uncertain, choose the more restrictive label and request human review.

---

# Professional profile

**PUBLIC-SAFE**

Michelle is an experienced full-stack software developer and IT development manager. Her core background includes C#, .NET, ASP.NET Core, SQL Server, Entity Framework Core, data integration, reporting, and business-system development. She has approximately 13 years of development experience and moved into development management while remaining deeply hands-on technically.

Her recent work increasingly combines traditional software engineering with AI-assisted development, agent workflows, architecture, data engineering, automation, computer vision, and robotics experimentation.

A useful narrative arc is:

**Developer → Manager → AI-Augmented Builder**

Do not publish employer staffing details, employee names, internal schedules, or organizational politics.

---

# Professional engineering systems

## Central Price Book / distributed store processing

**SANITIZE / ABSTRACT**

Michelle has designed and worked on a distributed price-book processing architecture supporting a multi-store retail environment. The system coordinates store-specific work across multiple worker machines, uses a central job-history/queue pattern, prevents duplicate processing, tracks worker claims and status, and supports operational troubleshooting.

Architectural themes that are safe to discuss in generalized form include:

- distributed workers
- atomic job claiming
- idempotency / duplicate prevention
- store-scoped workloads
- retry and failure handling
- operational status visibility
- orchestration of worker infrastructure
- separation of job orchestration from job execution

Do not publish store counts, internal service names, infrastructure identifiers, schedules, internal database/table names, vendor implementation details, or proprietary processing formats without explicit approval.

## POS / data platform

**SANITIZE / ABSTRACT**

Michelle has worked on retail data-platform architecture involving transactional sales, discounts, loyalty, fuel, item/store dimensions, ETL pipelines, staging, production loads, retry behavior, business-date replacement, and parity/validation checks.

Portfolio themes:

- dimensional modeling
- ETL design
- data quality
- transactional retail data
- repeatable business-date processing
- operational reliability
- reporting architecture

Do not publish internal schemas, table names, credentials, queries, customer data, or vendor-specific confidential implementation details.

## Merchandise ordering / replenishment

**SANITIZE / ABSTRACT**

Michelle has worked on an automated merchandise replenishment system combining sales history, inventory/on-hand data, in-transit quantities, item/vendor relationships, substitutions, promotions, and manager review/approval.

Portfolio themes:

- decision-support systems
- retail replenishment
- human approval over automated recommendations
- integrating multiple operational data sources
- handling store-specific exceptions

Do not publish vendor percentages, store identifiers, internal thresholds, or business-sensitive ordering rules.

## Fleet settlement / direct billing

**SANITIZE / ABSTRACT**

Michelle has worked on fleet settlement and invoicing workflows involving transaction repricing, customer discounts, billing periods, weekly invoicing, and multiple external transaction platforms.

Portfolio themes:

- billing workflows
- temporal business rules
- repricing
- external-system integration
- exception handling

Do not publish customer pricing, customer names, credentials, proprietary billing rules, or transaction data.

## Regulatory scan-data exports

**SANITIZE / ABSTRACT**

Michelle has developed and maintained regulated retail scan-data/export processing across multiple jurisdictions, integrating transaction history, product identifiers, loyalty information, promotional programs, and product-group mappings.

Portfolio themes:

- compliance-oriented data exports
- jurisdiction-specific rules
- complex data mapping
- transaction reconciliation
- scheduled data processing

Do not publish proprietary export specifications, customer/loyalty data, production SQL, or confidential vendor mappings.

## Workflow architecture

**SANITIZE / ABSTRACT**

Michelle has designed workflow concepts for business applications using explicit states, transitions, workflow instances, event history, and reliable outbound notification patterns. She has also worked on claims-based application security and sub-application architecture.

Portfolio themes:

- state machines
- auditable workflows
- approval systems
- claims-based authorization
- reliable notifications / outbox concepts

## Daily Performance

**SANITIZE / ABSTRACT**

Status: **Deployed / completed**.

A retail performance dashboard designed around recent sales performance, categories, fuel products, margins, and organizational drill-down from higher-level views into individual operating locations.

Do not expose internal financial values or proprietary reporting definitions.

## Early Sales

**SANITIZE / ABSTRACT**

Status: testing was completed and the supporting analyst query was ready as of September 2026. It supports a critical early-morning executive reporting process and replaced/deprecated a legacy manual data-hydration step.

Do not claim public deployment status beyond the facts above without confirmation.

## Fuel pricing work

**SANITIZE / ABSTRACT**

Michelle has worked on fuel-price analysis, a fuel-price matrix prototype/demo, and documentation for migration of real-time pricing processes. Some implementation work was handed to other development/integration resources.

Do not imply Michelle solely implemented components that were handed off to others.

---

# Mostly Human

**PUBLIC-SAFE**

Mostly Human is Michelle's emerging product concept/studio centered on software for ordinary human problems rather than technology searching for a problem.

The factory itself is an experiment in structured agent-assisted software development with planning, implementation, review, repair, testing, and explicit human control boundaries.

## I Did a Thing

**PUBLIC-SAFE**

Status: **In Development**.

A deliberately simple, human-centered product focused on recording things someone actually accomplished. The product is also being used as a practical test bed for the Mostly Human development factory and for simplifying UX through object-oriented UX thinking.

Do not mark this as shipped unless Michelle explicitly changes the status.

## Before I Forget

**PUBLIC-SAFE**

Status: **Ideation**.

A lightweight product concept centered on capturing things before they disappear from your brain.

Do not describe it as shipped or in development unless Michelle explicitly changes the status.

## Product-family direction

**PUBLIC-SAFE**

The intended model is to launch a small initial set of products and, after a real customer/user base exists, allow users to influence or vote on what gets built next.

Do not claim that customer voting currently exists.

---

# Mostly Human factory / agentic engineering

**PUBLIC-SAFE**, but avoid publishing credentials, private infrastructure, usage/billing details, or private repository material.

Michelle is actively experimenting with a software factory built around agent-assisted planning, implementation, review, and repair. Recent work includes:

- Archon-based orchestration
- PIV-style development loops
- specialized agent roles
- issue-driven implementation
- pull-request review
- independent review agents
- repair loops
- mutation testing
- test and validation gates
- Git safety
- model selection and cost awareness
- reducing review churn
- explicit human merge authority
- integrating OOUX/ORCA into product design before implementation

A central principle is:

**Agents may build and review. Michelle owns the final merge.**

The process is evolving. Do not present it as a finished methodology or universal best practice.

---

# OOUX / ORCA

**PUBLIC-SAFE**

Michelle identified UX/navigation design as a missing layer in her software-factory process and is incorporating Object-Oriented UX / ORCA thinking so agents model the objects, relationships, calls to action, and attributes of a product before generating navigation and screens.

This arose partly from observing that agents could make a fundamentally simple application unnecessarily complicated when allowed to invent UI structure without a strong object model.

This is an important theme for the How I Build section.

---

# Safety Claws

**PUBLIC-SAFE**

Safety Claws is an umbrella concept for passive software-safety tools.

Core philosophy:

**Observe. Detect. Explain. Don't silently change things.**

Potential/experimental directions include:

- import-file safety analysis
- CSV structural-change detection
- migration analysis
- configuration drift detection
- schema-change monitoring

Treat individual tools as concepts/experiments unless their status is explicitly documented elsewhere.

---

# Microduck robotics

## microduck_rl

**PUBLIC-SAFE**

This is the actual reinforcement-learning/training workspace for Microduck experiments.

Michelle's goals include teaching or experimenting with behaviors such as:

- hopping
- hopscotch
- balancing
- walking on a ball
- kicking
- locomotion

The work uses simulation/training tooling and is designed to accommodate a cloud/VPS-based workflow because Michelle does not rely on a local GPU.

Do not claim a behavior has been successfully trained unless there is explicit evidence/status confirming it.

## Duck Factory

**PUBLIC-SAFE**

Duck Factory is **not the training repository**.

It is telemetry, insight, and observability tooling for Microduck training. It helps inspect and understand training work but does not perform or launch the actual RL training runs.

Maintain this distinction everywhere in the portfolio.

## Interactive Microduck concept

**PUBLIC-SAFE / IDEATION**

Michelle has explored an interactive Microduck experience where a user could select trained behaviors such as hop, walk, or kick, potentially as part of a hopscotch-style interaction.

Treat this as an idea unless implementation status is explicitly confirmed.

---

# Pizza Vision

**PUBLIC-SAFE**, with implementation details reviewed before publication.

A computer-vision experiment involving pizza imagery/inference. Work has included Roboflow, local inference fallback, RF-DETR experimentation, and exploration of training approaches that do not require a local GPU.

A useful engineering story is the response to cloud inference cost changes: exploring local inference as a fallback and thinking about portability/cost rather than assuming hosted inference forever.

Do not publish private API details, usage credentials, or unsupported performance claims.

---

# Reachy Mini and robotics experimentation

**PUBLIC-SAFE**

Michelle has been exploring Reachy Mini and small robotics platforms as hands-on experiments in embodied AI, interaction, and agent-controlled behavior. Keep claims tied to actual experiments rather than implying completed production robotics systems.

---

# VPS / mobile development environment

**PUBLIC-SAFE**, with security-sensitive details removed.

Michelle has built and used a Linux VPS development environment that can be operated from an iPhone using SSH and persistent terminal sessions. It has been used for AI coding tools, repositories, and robotics-development workflows.

Portfolio themes:

- development from constrained/mobile environments
- Linux/VPS workflows
- SSH
- tmux/persistent sessions
- remote AI-assisted development

Never publish IP addresses, usernames, tokens, SSH material, API keys, or exact security configuration.

---

# AI engineering and tools

**PUBLIC-SAFE**

Michelle's practical AI-engineering work includes experimentation with:

- Claude Code
- OpenAI/Codex models and tooling
- Archon
- PIV development loops
- agent orchestration
- prompt/context design
- review agents
- evaluation and mutation testing
- RAG concepts
- long-term memory concepts
- production deployment considerations
- model routing and cost tradeoffs

Avoid presenting tool familiarity as formal expertise unless demonstrated by a project or artifact.

---

# Core engineering technologies

**PUBLIC-SAFE**

Strong professional background:

- C#
- .NET / ASP.NET Core
- SQL Server
- Entity Framework Core
- MVC / Razor-based web applications
- JavaScript
- REST/API integration
- SQL and data modeling
- ETL / SSIS
- reporting and data warehousing
- IIS
- Azure virtual machines
- Git / GitHub
- CI/CD concepts and implementation

Additional active experimentation:

- Python
- Linux
- MuJoCo
- reinforcement learning
- Hugging Face
- Weights & Biases
- Roboflow
- RF-DETR
- computer vision
- agentic software-development tooling

Do not use percentage-based skill meters.

---

# Engineering-management story

**PUBLIC-SAFE**, generalized.

Michelle moved from long-term hands-on development into IT development management while continuing to architect, troubleshoot, prototype, and write software. Her work increasingly spans implementation, architecture, project shaping, vendor/developer coordination, data systems, store/operational systems, and AI-assisted development practices.

Avoid publishing internal reporting structures, colleague names, staffing proposals, or confidential organizational plans.

---

# Portfolio storytelling principles

Agents should favor concrete engineering stories over generic claims.

Good:

- the problem
- constraints
- architecture
- tradeoffs
- what Michelle personally did
- what other people/teams did
- what changed
- what failed
- what was learned
- current status

Avoid:

- inflated leadership claims
- invented metrics
- claiming team work as solely Michelle's
- pretending prototypes shipped
- implying experiments succeeded without evidence
- exposing employer intellectual property
- turning every tool Michelle has tried into an “expert” skill

When facts are missing, insert a clear TODO/question for Michelle instead of inventing the answer.

---

# High-value initial portfolio stories

The strongest initial mix is likely:

1. **Mostly Human / agentic software factory** — shows current AI/software-process experimentation.
2. **Microduck RL + Duck Factory** — shows robotics, RL experimentation, and observability while preserving the distinction between training and telemetry.
3. **An anonymized distributed retail processing/data-system case study** — shows depth from Michelle's professional software-engineering career without exposing employer IP.

Supporting Field Notes can then document OOUX/ORCA, human merge authority, mutation testing, model-cost lessons, mobile/VPS development, and failures/repairs observed while building with agents.

---

# Accuracy rule

This catalog is a source of factual context, not permission to publish every detail.

For public content:

1. respect the publication label;
2. abstract professional details where required;
3. preserve explicit project statuses;
4. distinguish Michelle's work from work delegated or handed off to others;
5. never invent metrics or outcomes;
6. request human input when a story requires facts not contained here;
7. Michelle has final editorial and merge authority.
