---
title: Microduck RL and training observability
slug: microduck-rl
summary: "Reinforcement-learning experiments for Microduck, with training in microduck_rl and observability in Duck Factory."
description: "Reinforcement-learning experiments for Microduck, with training in microduck_rl and observability in Duck Factory."
kind: experiment
status: Experiment
featured: false
technologies: []
related_projects: []
related_notes: []
tags:
  - robotics
  - reinforcement-learning
  - observability
---

# Microduck RL and training observability

Reinforcement-learning experiments for Microduck, with training in microduck_rl and observability in Duck Factory.

**Status:** Experiment

**Kind:** Experiment

**My contribution:** I am experimenting with reinforcement learning for Microduck behaviors and a workflow that accommodates training without a local GPU.

TODO: Confirm which training, configuration, telemetry, and integration components Michelle personally implemented or adapted, and credit upstream work and collaborators where appropriate.

## Problem

My goals include experimenting with hopping, hopscotch, balancing, walking on a ball, kicking, and locomotion. These are behavior goals, not a list of completed capabilities.

The work also needs a way to inspect and understand training. Training and observability have distinct roles in this project.

## Context

I do not rely on a local GPU. The simulation and training workflow is designed to accommodate cloud/VPS-based work.

TODO: Confirm the actual simulation/training stack used in the run chosen for this story. Do not assign technologies from the general skills catalog to this project without project-specific confirmation.

## Architecture / Approach

| Workspace | Responsibility | Boundary |
| --- | --- | --- |
| `microduck_rl` | Actual reinforcement-learning and training workspace | Training runs occur here |
| Duck Factory | Telemetry, insight, and observability for Microduck training | Inspects training work; does not perform or launch RL training runs |

Duck Factory helps inspect and understand training work. It is distinct from the workspace where the actual training runs occur.

TODO: Add a reviewed diagram or artifact showing the actual telemetry path. The catalog does not establish transport, storage, update frequency, or the mechanism connecting the two workspaces.

## Decisions & Tradeoffs

The workflow accommodates the constraint of not relying on a local GPU. Training and observability are described separately so their responsibilities stay clear.

TODO: Confirm one actual design decision and its alternatives. For example, what led to a particular training environment or telemetry view? Do not claim cost savings, faster training, or improved results without evidence.

## Result / Current State

The catalog establishes an experiment and its intended behaviors. It does not establish that a particular behavior has been successfully trained, or whether any result has transferred from simulation to a physical robot.

An interactive experience in which a user selects behaviors remains an idea. It is not a demonstrated capability of either workspace.

TODO: Identify one training attempt to describe, including the goal, what was observed, whether it was simulation or physical hardware, and its current outcome. A failed or incomplete attempt is useful evidence too.

## Lessons

TODO: Add Michelle's observation from the selected attempt: what failed, what was surprising, what changed, or what remains uncertain. Do not turn the training/telemetry distinction into a claimed performance improvement.
