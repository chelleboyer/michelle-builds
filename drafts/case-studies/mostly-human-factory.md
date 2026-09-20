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

**My contribution:** I am experimenting with the factory's development process, incorporating OOUX/ORCA into product design, and retaining final merge authority.

## Problem

Mostly Human is my emerging product studio, centered on software for ordinary human problems. The factory is an experiment in how to develop those products with agents while keeping planning, validation, review, and human decisions explicit.

One problem I identified was a missing UX design step. When agents could invent screens and navigation without a strong object model, they could make a fundamentally simple application unnecessarily complicated.

## Context

**I Did a Thing**, a product for recording things someone actually accomplished, is **In Development**. It is also a practical test bed for the factory and for simplifying UX through object-oriented UX thinking.

**Before I Forget**, a lightweight concept for capturing things before they disappear from your brain, is in **Ideation**. These products have different lifecycle states from the factory experiment itself.

## Architecture / Approach

The process combines Archon-based orchestration and PIV-style development loops. My experiments include specialized agent roles, issue-driven implementation, pull-request review, independent review agents, repair loops, mutation testing, and validation gates.

The intended sequence is:

1. Shape the idea and brief.
2. Model objects, relationships, calls to action, and attributes before generating navigation and screens.
3. Plan small work issues and implement changes with agents.
4. Validate the changes, review the pull request independently, and repair findings.
5. Bring the change to human review and a human-owned merge decision.

This describes the evolving process, not evidence that every experimental run has followed every step successfully.

## Decisions & Tradeoffs

**Model the product before generating its screens.** I am incorporating OOUX/ORCA to give agents an explicit object model before they propose navigation. This responds to observed UX complexity in otherwise simple applications.

**Keep merge authority with the human.** Agents may implement, validate, review, and propose repairs. I own the final merge. The workflow retains that decision even when agents perform much of the development work.

TODO: Add one specific, confirmed tradeoff from an actual factory run: what changed, what it cost, and why that choice was worthwhile. Do not infer a result from the list of tools or practices.

## Result / Current State

The factory is an active experiment. Current areas of work include model selection, cost awareness, Git safety, context management, reducing review churn, and integrating object-oriented UX into planning.

The product test bed remains in development. This case study does not yet establish a measured change in delivery speed, quality, cost, or user outcomes.

TODO: Select one public or sanitized artifact that demonstrates an actual planning → implementation → review → repair sequence, with Michelle's contribution distinguished from agent work.

## Lessons

UX design needed an explicit place in the process. Observing unnecessary complexity in a simple application led me to incorporate object modeling before screen and navigation generation.

The methodology is still evolving. A workflow description alone is not evidence that its gates improve outcomes.

TODO: Confirm one concrete example of the OOUX lesson or another factory lesson, including what was observed after the change.
