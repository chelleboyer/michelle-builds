---
title: "Human-owned merge decisions"
slug: human-merge-authority
summary: "Agents may build and review; I own the final merge."
description: "Agents may build and review; I own the final merge."
maturity: "Established boundary in an evolving process"
related_projects: []
related_notes: []
---

# Human-owned merge decisions

Agents may build and review; I own the final merge.

**Maturity:** Established boundary in an evolving process

## Problem

Implementation, passing checks, and review findings are inputs to an acceptance decision. They do not transfer responsibility for that decision to an agent.

## Practice

Agents may plan, implement, test, review, and propose repairs. I retain final review and merge authority. Release remains a separate human decision.

A failed check or an unresolved finding stays visible. Agents must not bypass gates, silently weaken tests, or declare a release shipped.

## Rationale

This keeps human judgment at the boundary where proposed work becomes accepted work. The process can use substantial agent autonomy while preserving a clear owner for that decision.

## Evidence & Limits

Human merge authority is an explicit principle of my Mostly Human factory experiments. It is a control boundary, not a guarantee that every accepted change is correct. The process still depends on meaningful validation and review.

## Related work

- [Fresh review after repair](fresh-review-after-repair.md)
- [The complete workflow](index.md#the-workflow)
