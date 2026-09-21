---
title: "Objects before screens"
slug: objects-before-screens
summary: "Model the things a product contains and their relationships before generating navigation and screens."
description: "Model the things a product contains and their relationships before generating navigation and screens."
maturity: "Being incorporated into the development process"
related_projects: []
related_notes: []
---

# Objects before screens

Model the things a product contains and their relationships before generating navigation and screens.

**Maturity:** Being incorporated into the development process

## Problem

I observed agents make a fundamentally simple application unnecessarily complicated when they could invent navigation without a strong object model. UX design needed an explicit place before implementation.

## Practice

I am incorporating OOUX/ORCA into product design. Before proposing screens, identify:

- **Objects:** the things people need to understand or work with.
- **Relationships:** how those things connect.
- **Calls to action:** what people need to do with them.
- **Attributes:** the information each thing needs.

Use that model to propose the smallest viable navigation, then bring the architecture to human review before implementation.

## Rationale

An object model gives navigation a concrete basis. The design gate is intended to avoid later navigation rework; it is not a claim of proven cost savings.

## Evidence & Limits

I Did a Thing, which remains **In Development**, is a practical test bed for the Mostly Human factory and for simplifying UX through object-oriented thinking. The observation of unnecessary complexity led me to add object modeling to the process.

The approach is still being incorporated. A model and an approval gate do not replace observing whether people can use the resulting product.

## Related work

- [Human-owned merge decisions](human-merge-authority.md)
- [Fresh review after repair](fresh-review-after-repair.md)
- [The complete workflow](index.md#the-workflow)
