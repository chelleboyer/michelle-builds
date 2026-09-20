# PR #5 — Review after independent-review repairs

Historical review of `711d668`; both findings below are resolved by the human-confirmed repairs and catalog synchronization.
See the [current complete review](pr-5-complete-review.md) for the present disposition.

Reviewed head: `711d6682c0844108aee9a1fd3ccea2febc85c75c`.
Previous local head: `eb2491f645e35f3a7582051c542ca3c45077bdfb`.

Fast-forwarded the branch and reviewed all three incoming commits plus the full
three-draft package against AGENTS.md, the brief, the catalog, and content guide.
This is a follow-up review by the implementing agent, not a new independent review.
All reviewer-owned files are preserved without edits or reversions.

## Findings and disposition

### Medium — New factual context is not yet reflected in the curated catalog

Locations: `drafts/case-studies/microduck-rl.md:29`,
`drafts/case-studies/mostly-human-factory.md:60`, and
`context/MICHELLE-WORK-CATALOG.md:267`.

The repairs introduce Michelle's working lab fork and a specific factory incident.
The catalog still describes the earlier Microduck workspace arrangement and
contains only general factory-review topics. This is a source synchronization gap:
the added lab does not inherently contradict microduck_rl's role as a training
workspace, and Duck Factory's explicit no-training boundary remains intact.

Disposition: human editorial follow-up before publication. Preserve the supplied
reviewer context, record its provenance, and incorporate confirmed additions into
the catalog rather than letting future agents infer that context from draft prose.
The factory incident's public/sanitized artifact is already an open question in
`design/CASE-STUDY-REVIEW.md`; do not reopen it as a request to invent another story.
Repository documentation supports lab capabilities, not Michelle's run results or
proof of which components she implemented.

### Low — Comparative cost phrasing lacks evidence

Location: `drafts/case-studies/mostly-human-factory.md:58`.

“The gate is intentionally cheaper” states a cost comparison, while the same draft
explicitly does not claim measured cost improvement. No supporting comparison is
provided in the catalog or review package.

Disposition: human editorial follow-up; reviewer text is unchanged. Proposed wording
for consideration: “It adds a design gate intended to avoid reworking navigation
after implementation.” This preserves the rationale without asserting a cost result.
Alternatively retain a comparative claim only with appropriate evidence.

## External verification

GitHub reports `chelleboyer/microduck-lab` as public and forked from
[`jonathanhawkins/microduck-lab`](https://github.com/jonathanhawkins/microduck-lab).
The working fork's README was inspected at commit
[`3f788f3c79f86696e95c5e6877cffd9e2ea19628`](https://github.com/chelleboyer/microduck-lab/blob/3f788f3c79f86696e95c5e6877cffd9e2ea19628/README.md).
It documents CPU MuJoCo, Stable Baselines 3 PPO, Linux support, a shared deployment
interface, and prototyping followed by retraining in the official stack for
sim-to-real work. Its demonstrations and performance numbers were not attributed
to Michelle. The upstream identity is now available for artifact attribution;
additional collaborator credit remains a human question.

No concrete factory-run artifact was linked in the incoming commits. The supplied
incident account is retained as reviewer-provided context, not independently
verified as a specific run by this follow-up.

## Validation — PASS

- `python -m pip check`: passed.
- `python -m mkdocs build --strict`: passed.
- `git diff --check origin/main...HEAD`: passed.
- Draft checks: all three YAML blocks parse; slugs, headings, statuses, and
  descriptions agree; Markdown renders. Summary comparison normalizes inline code
  formatting rather than treating backticks as a factual mismatch.
- Generated-output check: all 153 local link/asset references resolve.
- Review-package links resolve.
- Draft routes, TODOs, and source/report directories stay out of generated HTML,
  search JSON, and sitemap.
- CI at reviewed head: build passed; deploy skipped as designed.

The repository has no separate application test, lint, or type-check suite.
No checks were weakened and no unrelated tests or dependencies were introduced.

## Handoff

The repairs are retained. Technical validation passes; the findings above are
editorial follow-ups, not build defects. Existing questions about the retail
lifecycle/contribution and selected artifacts remain open. Do not promote drafts
to `docs/`, mark artifact-backed case studies complete, merge, or deploy as part
of this review. Michelle owns the next editorial and merge decisions.
