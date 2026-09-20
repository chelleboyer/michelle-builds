# Implementation report — Initial case-study drafts

Plan: `design/ARCHITECTURE-ORCA.md`, work unit 3.
Branch: `feat/initial-case-studies`.
Status: Draft package complete; public case-study pages pending factual/editorial review.

## Changes

Three Markdown skeletons in `drafts/case-studies/` cover Mostly Human factory,
Microduck RL with Duck Factory, and generalized distributed retail processing.
Each has the project metadata and six case-study sections. Supported prose is
written; missing facts and artifacts are explicit TODOs. The editorial review
matrix maps claims to catalog sections and identifies proposed public paths.
README links to the review package.

## Validation

- Strict MkDocs build and dependency consistency checks passed.
- All three draft front-matter blocks parse, match filenames, and keep visible
  summary/status consistent with metadata; required sections render as Markdown.
- Review-package file links resolve.
- Draft paths, TODOs, and source directories are absent from HTML, search JSON,
  and sitemap output.
- Whitespace check passed.

No permanent tests added for editorial drafts. No production-code, dependency,
configuration, navigation, or deployment change.

## Deliberate scope decision

The content guide requires incomplete case studies to stay outside `docs/`.
The retail lifecycle, detailed contributions, and several outcomes/lessons are
not established in the catalog. These drafts therefore do not create public
pages or imply the MVP's three artifact-backed stories are complete. Michelle
was asked for the most consequential missing facts; remaining questions are in
`design/CASE-STUDY-REVIEW.md`.

## Self-review

Checked prose against the catalog and brief. No invented metrics, completed
robot behaviors, lifecycle promotions, private repository URLs, or sole-authorship
claims found. Factory and Microduck Experiment states reflect explicit experiment
descriptions; the retail status is an unresolved TODO. Professional material is
generalized. Duck Factory remains telemetry/observability, never a training launcher.

Independent review and Michelle's factual/editorial review remain pending.
No merge or release action performed.
