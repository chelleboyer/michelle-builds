# Implementation report — How I Build

Plan: `design/ARCHITECTURE-ORCA.md`, work unit 4.
Branch: `feat/build-process`. Status: COMPLETE.

## Changes

Added three Markdown Build Practices: human-owned merge decisions, fresh review
after repair, and objects before screens. Expanded How I Build with the intended
workflow, a static SVG diagram, a complete ordered text equivalent, and links to
the practices. Added scoped image sizing CSS and updated README progress.

## Content and implementation review

Claims were checked against the brief and the confirmed factory/OOUX catalog
sections. The process is explicitly evolving; no measured productivity, cost, or
quality improvement is claimed. The repair-loop observation is human-confirmed.
Product status remains In Development. The diagram includes architecture approval,
repair/revalidation, fresh review, human merge, and a separate release decision.
Case-study drafts and source context are unchanged and remain outside site input.

Self-review found no blocking issues. This is not an independent review.

## Validation

- Strict MkDocs build and dependency check passed.
- All 315 generated local link, asset, and anchor references resolve.
- Practice front matter, visible summaries/maturity, and routes checked.
- SVG parses, includes title/description, contains no scripts, and has meaningful
  HTML alt text plus a full adjacent text equivalent.
- SVG rendered and visually inspected at 360 px width: labels and loop arrows fit.
- Source/catalog/draft directories remain outside site output.
- Diff whitespace check passed.

The initial Cairo preview attempt failed because a system library was missing.
An isolated temporary resvg renderer with an explicit local font successfully
produced the inspected preview. No preview tools were added to project dependencies.
Full browser/mobile/accessibility review remains in work unit 5.

## Deliberate implementation choices

Static SVG keeps the diagram available without a client-side Mermaid dependency.
Content remains Markdown; no navigation configuration or new framework is needed.
Practice links are curated in the How I Build index as the content guide specifies.
Publication and merge remain human decisions.
