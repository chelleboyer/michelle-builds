---
title: Mostly Human factory
slug: mostly-human-factory
summary: "An experiment in agent-assisted software development with planning, review, repair, and human control boundaries."
description: "An experiment in agent-assisted software development with planning, review, repair, and human control boundaries."
kind: experiment
status: Experiment
featured: false
technologies:
  - Archon
related_projects: []
related_notes: []
tags:
  - agent-assisted-development
  - product-development
  - ooux
---

# Mostly Human factory

An experiment in agent-assisted software development with planning, review, repair, and human control boundaries.

**Status:** Experiment

**Kind:** Experiment

**My contribution:** I am designing and testing the factory's development process, incorporating OOUX/ORCA into product design, reviewing its outputs, and retaining final merge authority.

## Problem

Mostly Human is my emerging product studio, centered on software for ordinary human problems. The factory is an experiment in how to develop those products with agents while keeping planning, validation, review, and human decisions explicit.

Two failure modes became especially useful. First, agents could invent screens and navigation without a strong object model and make a fundamentally simple application unnecessarily complicated. Second, a repair loop could become too narrow: after repairing known findings, rechecking only those findings could miss additional problems that a fresh review would have found.

## Context

**I Did a Thing**, a product for recording things someone actually accomplished, is **In Development**. It is also a practical test bed for the factory and for simplifying UX through object-oriented UX thinking.

**Before I Forget**, a lightweight concept for capturing things before they disappear from your brain, is in **Ideation**. These products have different lifecycle states from the factory experiment itself.

## Architecture / Approach

The process combines Archon-based orchestration and PIV-style development loops. My experiments include specialized agent roles, issue-driven implementation, pull-request review, independent review, repair loops, mutation testing, validation gates, and explicit human merge authority.

The intended sequence is:

1. Shape the idea and brief.
2. Model objects, relationships, calls to action, and attributes before generating navigation and screens.
3. Plan small work issues and implement changes with agents.
4. Validate the complete change and review the pull request independently.
5. Repair findings, then perform a fresh review of the resulting change rather than merely checking that the previously known findings disappeared.
6. Bring the change to human review and a human-owned merge decision.

This describes the evolving process, not evidence that every experimental run has followed every step successfully.

## Decisions & Tradeoffs

**Model the product before generating its screens.** I am incorporating OOUX/ORCA to give agents an explicit object model before they propose navigation. This responds to observed UX complexity in otherwise simple applications. It adds a design gate, but the gate is intentionally cheaper than repairing a navigation model after implementation.

**Fresh review after repair.** In one factory run, the repair stage addressed the findings it had been given, but the next broader review surfaced additional issues, including ordering, identity/email-normalization, password-length, and factory-level review concerns. That exposed a process flaw: verifying only the known findings after a repair is not equivalent to reviewing the repaired change. The factory therefore treats repair as producing a new review candidate rather than as proof that the work is complete.

**Keep merge authority with the human.** Agents may implement, validate, review, and propose repairs. I own the final merge. The tradeoff is intentional friction at the boundary where a change becomes accepted work.

## Result / Current State

The factory is an active experiment. It now has concrete process safeguards derived from its own failures: object modeling before UI/navigation generation, fresh review after repairs, validation gates, and human-owned merge decisions.

The product test bed remains in development. This case study does not claim a measured change in delivery speed, quality, cost, or user outcomes. The evidence is narrower: the factory has surfaced defects in its own workflow and those findings have changed the workflow.

A useful artifact for this story is the PR/review trail from a factory run that shows implementation, findings, repair, and the subsequent broader review. Publication should use only a reviewed public PR or sanitized excerpt.

## Lessons

A repair loop can create false confidence if it only asks whether known findings were fixed. A repaired change needs a fresh complete review because the repair can expose or leave unrelated problems.

UX design also needs an explicit place in the process. Observing unnecessary complexity in a simple application led me to incorporate object modeling before screen and navigation generation.

The broader lesson is that the factory itself is part of the product being tested. Agent autonomy is useful only when the surrounding process can reveal when an agent has satisfied a narrow instruction without satisfying the larger engineering goal.
