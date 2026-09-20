# Writing content for Michelle Builds

This guide implements work unit 2 of the [approved architecture](ARCHITECTURE-ORCA.md).
Projects, Field Notes, and Build Practices are ordinary Markdown files. Adding an
entry requires editing content and its index, not Python, JavaScript, templates,
or `mkdocs.yml`. The six top-level navigation destinations remain stable.

## Draft, review, then include in the site

1. Read the [brief](../PORTFOLIO-BRIEF.md) and
   [work catalog](../context/MICHELLE-WORK-CATALOG.md).
2. Copy a template into a draft folder **outside `docs/`**, such as
   `drafts/<slug>.md`. Keep factual questions there until resolved. This excludes
   drafts from the site, not from repository visibility: never commit secrets or
   confidential source material anywhere in the repository.
3. Replace every TODO with supported content, or remove optional sections. If a
   lifecycle state, contribution, result, or lesson is unknown, ask Michelle;
   do not fill the gap from repository activity. Keep the draft outside `docs/`.
4. Prepare sanitized public copy for review. Publication labels belong in the
   review context, not in public front matter. `SANITIZE / ABSTRACT` needs
   generalization; `CONTEXT-ONLY` needs explicit human approval.
5. Put only publication-ready copy and assets in `docs/` on a feature branch,
   update the Markdown index, and validate. Michelle's editorial review and merge
   decide whether it belongs in the site; deployment remains a separate human action.

**Everything in `docs/` is public build input.** Omitting a page from navigation,
setting `draft: true`, adding `published: false`, or writing an HTML comment does
not protect it. We have no draft-exclusion plugin. Metadata is not a privacy boundary.

## Choose a template and location

| Object | Template | Public path | Entry point |
| --- | --- | --- | --- |
| Project | [project.md](../templates/project.md) | `docs/work/<slug>.md` or `docs/lab/<slug>.md` | Work or Lab index |
| Field Note | [field-note.md](../templates/field-note.md) | `docs/notes/<slug>.md` | Field Notes index, newest first |
| Build Practice | [build-practice.md](../templates/build-practice.md) | `docs/how-i-build/<slug>.md` | How I Build index |

Use one canonical page per object. Work holds professional and product case
studies; Lab holds experiments. Editorial placement need not follow lifecycle
state. Cross-link a project from both indexes when helpful instead of duplicating
it. Product, Experiment, and System do not need extra page engines.

Use lowercase, hyphenated, stable slugs. A filename such as `lab/example-project.md`
produces `/michelle-builds/lab/example-project/`. MkDocs uses the **file path**,
not the `slug` metadata, for URLs. Keep the slug equal to the filename stem and
unique across projects so relationship references are unambiguous. Avoid moving
published pages just because their status changes.

## Metadata contract

This contract applies to individual Projects, Field Notes, and Build Practices.
Section entry pages use only `title` and `description`; Home may use the site
name as its metadata title and Michelle's name as its H1.

These are authoring conventions reviewed in the PR, not an automated schema.
MkDocs parses YAML and validates links; it does not validate our custom fields.

| Field | Applies to | Convention |
| --- | --- | --- |
| `title` | All | Required string; match the single H1 |
| `slug` | All | Required stable filename stem |
| `summary` | All | Required short, factual string; repeat in the visible introduction |
| `description` | All | Required string matching the summary; used by the theme for page metadata |
| `kind` | Project | Required: `professional`, `product`, or `experiment` |
| `status` | Project | Required, explicitly confirmed lifecycle state |
| `featured` | Project | Boolean; defaults to `false`; editorial intent, not automatic homepage inclusion |
| `technologies`, `tags` | Project; tags also on Note | Lists of strings; omit unsupported tool claims |
| `started`, `updated` | Project | Optional quoted ISO date (`YYYY-MM-DD`); omit unknown dates |
| `repository`, `demo` | Project | Optional verified public HTTPS URLs; omit unavailable/private links |
| `date` | Field Note | Required quoted ISO publication date; display it in the body too |
| `maturity` | Build Practice | Required concise, confirmed description of how established the practice is |
| `related_projects` | All | List of existing project slugs; empty list allowed |
| `related_notes` | Project, Build Practice | List of existing note slugs; empty list allowed |

Project states follow the approved design: `Ideation`, `Prototype`, `Experiment`,
`In Development`, `Testing`, `Shipped`, `Paused`, `Archived`, or the exact confirmed
professional completion/deployment wording. Preserve catalog distinctions such as
`Deployed / completed`; do not equate completed testing with deployment.

Custom metadata is **not automatically displayed**, sorted, filtered, linked, or
used to create cards. Put status, role, relevant technologies, dates, repository
links, and relationships in visible Markdown as appropriate. Keep metadata and
visible text in sync during review. This small amount of manual curation is
intentional until repeated content justifies automation.

## Link an entry into the site

A new page can be built without adding it to `mkdocs.yml`. Link to it from its
section index so people can discover it. MkDocs may print an informational notice
that it is outside the explicit navigation; it still renders and enters search.

For example, after creating a reviewed `docs/lab/example-project.md`, add this
pattern under the Lab index's projects heading (replace all example text):

```markdown
### [Project title](example-project.md)

One factual sentence explaining the project.

**Status:** Confirmed status · **My contribution:** Confirmed role
```

For a note, add a dated link and short summary under Recent notes, newest first.
For a practice, add a link and summary under Practices. Replace the empty-state
sentence when the first real entry is added. Curate a few links on Home when
there is reviewed work to feature; `featured: true` alone has no visual effect.

Use relative `.md` links: from a note, `../lab/example-project.md`; from Home,
`lab/example-project.md`. Relationship metadata uses slugs, but visible links
use relative file paths. Maintain reciprocal links when useful, not automatically.
Never add dead links to planned pages or guessed repository URLs.

## Readable pages and artifacts

Use one H1 followed by descriptive H2 sections. Projects follow Problem, Context,
Architecture / Approach, Decisions & Tradeoffs, Result / Current State, and
Lessons. A short note may use fewer headings. Keep lifecycle and personal
contribution visible near the top of a project.

Store approved artifacts under `docs/assets/images/<project-slug>/`. Use relative
paths and descriptive alt text. Describe diagrams in nearby prose; avoid making
an image the only source of information. Use fenced code blocks with a language
label, and only publish code cleared for public use. Do not add stock imagery to
fill an empty section.

The Home, Work, Lab, How I Build, Field Notes, and About pages are curated entry
points. Their headings and empty states support gradual publication without
fictitious cards, dates, metrics, contact details, or résumé links.

## Validate and review

```bash
python -m pip check
python -m mkdocs build --strict
python -m mkdocs serve
```

Preview the new page, its index link, and its related links. Check narrow-screen
readability, visible status/date/role, headings, artifact descriptions, and factual
attribution. Strict builds catch broken Markdown links, not unsupported claims,
private information, unknown lifecycle states, or stale duplicate metadata.
Review those explicitly against the catalog before Michelle's final review.
