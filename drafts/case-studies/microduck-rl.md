---
title: Microduck training lab and observability
slug: microduck-rl
summary: "Reinforcement-learning experiments for Microduck using a fast Microduck Lab experimentation loop, with microduck_rl as the graduation target and Duck Factory for observability."
description: "Reinforcement-learning experiments for Microduck using a fast Microduck Lab experimentation loop, with microduck_rl as the graduation target and Duck Factory for observability."
kind: experiment
status: Experiment
featured: false
technologies:
  - MuJoCo
  - Stable-Baselines3
  - PPO
related_projects: []
related_notes: []
tags:
  - robotics
  - reinforcement-learning
  - observability
---

# Microduck training lab and observability

Reinforcement-learning experiments for Microduck using a fast Microduck Lab experimentation loop, with `microduck_rl` as the graduation target and Duck Factory for observability.

**Status:** Experiment

**Kind:** Experiment

**My contribution:** I am adapting a forked Microduck Lab into my working experimentation environment for behavior design and training, while building a workflow that does not depend on a local GPU.

The working fork is public at `chelleboyer/microduck-lab`. It is based on upstream Microduck Lab work and should retain upstream credit rather than being presented as an original robot/training stack.

## Problem

My goals include experimenting with hopping, hopscotch, balancing, walking on a ball, kicking, and locomotion. These are behavior goals, not a list of completed capabilities.

I also need a development loop that is fast enough for behavior experimentation while preserving a path toward the more complete Microduck training stack and physical-robot work.

## Context

I do not rely on a local GPU. The current lab is designed around CPU-friendly MuJoCo experimentation with Stable-Baselines3/PPO and can be operated from a Linux VPS. The lab preserves the Microduck observation/action/control contract so experiments are not disconnected from the robot's training interface.

The progression is intentionally incremental: balance/recovery and hopping are useful foundations before compound behaviors such as hopscotch. These are training stages and goals, not claims that the physical robot has mastered them.

## Architecture / Approach

| Workspace | Responsibility | Boundary |
| --- | --- | --- |
| `chelleboyer/microduck-lab` | Working fork and fast experimentation loop for environments, rewards, behavior definitions, training configuration, evaluation, and experiment artifacts | Used to design and evaluate behaviors quickly; upstream work is credited |
| `microduck_rl` | Graduation target for successful behaviors | Behaviors that prove useful in the lab must be ported/retrained in the official training stack, including the more realistic sim-to-real work, before physical deployment is claimed |
| Duck Factory | Telemetry, insight, and observability | Inspects training work; does not perform or launch RL training runs |
| Archon | Factory/orchestration layer around the experimentation repo | Organizes the engineering workflow; it is not part of the robot runtime |

This separation is deliberate. The lab is the fast design loop, `microduck_rl` is the path toward the production-quality training environment, and Duck Factory is for understanding what training is doing. A convenient experiment is not automatically a deployable robot behavior.

## Decisions & Tradeoffs

The main tradeoff is iteration speed versus simulation fidelity. A lighter CPU-friendly lab makes it easier to change rewards, environments, and behavior ideas without waiting on a heavyweight training loop or local GPU. The cost is that success in that lab is only evidence for the next stage, not proof of sim-to-real success.

Keeping the working fork separate also gives the factory a clear source of truth for experiment definitions while allowing successful ideas to graduate deliberately rather than silently changing the upstream/official training workspace.

## Result / Current State

The project is an active experiment. The new `chelleboyer/microduck-lab` fork is now the working behavior-development repository, with MuJoCo/SB3/PPO as the fast experimentation loop. `microduck_rl` remains the graduation target for behaviors that earn further investment, and Duck Factory remains separate observability tooling.

No statement here claims that hopping, hopscotch, balancing on a ball, kicking, or other target behaviors have successfully transferred to the physical robot. A concrete training run/result should be added once it has been reviewed as an artifact-backed example.

## Lessons

Separating the fast experimentation loop from the higher-fidelity graduation path makes the evidence boundary clearer: a behavior can be promising in the lab without being described as a finished robot capability. Keeping observability separate from training execution similarly makes each repository's responsibility easier to reason about.

The next useful evidence for this case study is a reviewed training artifact—successful, incomplete, or failed—that shows what changed in response to an actual run.
