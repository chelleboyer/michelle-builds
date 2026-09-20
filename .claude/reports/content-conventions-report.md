# Implementation Report — Content conventions

**Plan:** design/ARCHITECTURE-ORCA.md, work unit 2

**Branch:** feat/content-conventions

**Status:** COMPLETE

## Summary

Added reusable Markdown templates and an authoring guide covering metadata,
visible fields, stable URLs, relationships, publication boundaries, and manual
index curation. Expanded the six entry pages with metadata and content sections,
preserving honest empty states until case studies and notes are ready.

## Tasks completed

- Create `templates/project.md`, `templates/field-note.md`, and `templates/build-practice.md`.
- Create `design/CONTENT-GUIDE.md` and link it from README authoring instructions.
- Update the six section/Home pages with metadata and curated section headings.

## Tests and validation

- `python -m mkdocs build --strict`: passed.
- `python -m pip check`: passed.
- Temporary-copy authoring exercise: one page from each template built with an
  unchanged `mkdocs.yml` and Markdown index links; all three output routes existed.
- Negative check: a link to `missing-page.md` failed the strict build as expected.
- Template front matter parsed as YAML; templates and guide remained outside site output.
- Generated HTML: 153 local links/assets resolve; each entry page has one H1 and
  a description; no TODOs or source/template/report directories are published.
- `git diff --check`: passed.

No permanent test suite added for this Markdown-only change. Temporary fixtures
were isolated from the working tree and removed after verification. Browser and
mobile visual review remain part of work unit 5; no visual-review claim is made.

## Deviations from the plan

No new runtime renderer or automatic index generator: the approved design calls
for conventional Markdown until repetition demonstrates a need. The guide makes
manual synchronization of metadata and visible content explicit. Added theme
`description` metadata alongside the proposed editorial `summary` field.

## Review and remaining work

Self-review recorded in `.claude/code-reviews/content-conventions.md`.
Independent review remains pending. Work units 3–6 remain separate: case studies,
workflow diagram/practices, visual review, and release validation. No deployment
or merge performed.
