---
title: "Fresh review after repair"
slug: fresh-review-after-repair
summary: "A repair produces a new review candidate, not proof that the work is complete."
description: "A repair produces a new review candidate, not proof that the work is complete."
maturity: "Practice shaped by a confirmed factory failure"
related_projects: []
related_notes: []
---

# Fresh review after repair

A repair produces a new review candidate, not proof that the work is complete.

**Maturity:** Practice shaped by a confirmed factory failure

## Problem

A repair loop can become too narrow. Checking only whether known findings disappeared can leave other problems outside the review's attention.

## Practice

After repairs, validate the resulting change and review it as a whole. Revisit the requirements, behavior, and surrounding context as well as the original findings. Keep independent review distinct from the implementer's own checks.

If that review finds more issues, return to repair and validation. A clean result still goes to human review; it does not authorize an agent to merge.

## Rationale

The repaired change is the thing being proposed for acceptance. The original finding list is useful context, but it is not a complete description of what can go wrong in that change.

## Evidence & Limits

In one Mostly Human factory run, a repair stage addressed its known findings. A subsequent broader review surfaced additional concerns, including ordering, identity/email normalization, password length, and the review process itself.

That experience informed this practice. It supports the need to review beyond a fixed finding list; it does not establish a measured improvement in quality, delivery speed, or cost.

## Related work

- [Human-owned merge decisions](human-merge-authority.md)
- [Objects before screens](objects-before-screens.md)
- [The complete workflow](index.md#the-workflow)
