# Michelle Builds

**Developer → Manager → AI-Augmented Builder**

Things I build, systems I run, experiments I probably shouldn't have started at 5 AM.

This repository is the source for a living technical portfolio: part engineering portfolio, part field journal, part laboratory.

## What belongs here

- **Work** — production software, architecture, data systems, and engineering case studies
- **Lab** — AI engineering, robotics, computer vision, and other experiments
- **Products** — Mostly Human and Safety Claws projects as they develop
- **How I Build** — the evolving human + agent software-development process
- **Field Notes** — short technical observations, lessons, failures, and discoveries

## Build philosophy

The site should prove capability through real artifacts rather than skill meters or marketing claims. It should stay content-first, static where practical, Markdown-driven, accessible, fast, and easy to maintain.

Before implementation, read `PORTFOLIO-BRIEF.md` and `AGENTS.md`.

## Current phase

**Content structure and authoring conventions.** Michelle merged the [ORCA and architecture proposal](design/ARCHITECTURE-ORCA.md) in [PR #1](https://github.com/chelleboyer/michelle-builds/pull/1). The foundation provides navigation and section introductions; reusable Markdown templates and the [content guide](design/CONTENT-GUIDE.md) support the next case studies and Field Notes. Final visual design remains a subsequent work unit.

## Reference

Architectural inspiration: `skyejen/generalist-tech`. Use it as a reference, not as content, branding, or an information architecture to copy.

## Local development

Use Python 3.12:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m mkdocs serve
```

Open http://127.0.0.1:8000/michelle-builds/ for the local preview.

Validate before proposing changes:

```bash
python -m pip check
python -m mkdocs build --strict
```

The generated `site/` directory is disposable and ignored by Git. Only `docs/`
is published; the brief, factual catalog, and design documents stay outside the
site input directory. Keep reviewed public copy and approved assets in `docs/`.
Do not copy private source material there.

## Add content

Start with the [content guide](design/CONTENT-GUIDE.md) and the templates in
`templates/`. Draft outside `docs/`; move only reviewed public copy into the site.
Add a relative Markdown link in the appropriate section index. No application-code
or navigation-configuration changes are needed for individual entries.

Custom front matter records editorial metadata; visible summaries, status, dates,
and related links are ordinary Markdown and must be kept in sync. Indexes are
manually curated for the MVP.

## Publication

The Site workflow builds pull requests and changes to `main` and uploads the
static Pages artifact. Publication is a separate, human-triggered action:

1. Review and merge the change.
2. Configure repository Settings → Pages → Source to **GitHub Actions**.
3. Configure the `github-pages` environment for required human review where available.
4. After editorial and release review, run the **Site** workflow manually on `main`.

PR builds and ordinary pushes do not deploy. The target URL is
https://chelleboyer.github.io/michelle-builds/. A custom domain would require an
explicit configuration change. Agents do not trigger release workflows.

## Next work

Follow the remaining [implementation work units](design/ARCHITECTURE-ORCA.md#13-implementation-work-units-after-approval):
reviewed case studies, the workflow diagram, responsive and
accessibility review, and final release validation. The current foundation is
not a declaration that the portfolio is ready to publish.
