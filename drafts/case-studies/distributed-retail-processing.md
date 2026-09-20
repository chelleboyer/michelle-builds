---
title: Coordinating distributed retail processing
slug: distributed-retail-processing
summary: "Centralizing a location-specific vendor workflow by coordinating a fleet of workers that reproduce the existing store process."
description: "Centralizing a location-specific vendor workflow by coordinating a fleet of workers that reproduce the existing store process."
kind: professional
status: "In development / integration"
featured: false
technologies: []
related_projects: []
related_notes: []
tags:
  - distributed-processing
  - orchestration
  - operational-reliability
---

# Coordinating distributed retail processing

Centralizing a location-specific vendor workflow by coordinating a fleet of workers that reproduce the existing store process.

**Status:** In development / integration

**Kind:** Professional

**My contribution:** I designed the distributed-processing and orchestration approach, including the central job/history model, worker-claiming and duplicate-prevention concepts, the VM-manager/orchestration design, and hands-on development and testing around automating the existing location-side application. Other contributors own or support adjacent ETL, data-loading, and downstream pieces; this is not presented as a solo implementation.

## Problem

A required vendor-side change could not move at the speed the business needed. Rather than wait for the vendor or replace the existing location process, I designed a way to run that process centrally while preserving the behavior of what an individual location already does.

The challenge therefore became orchestration: reproduce location-specific execution across a fleet of worker VMs, coordinate which location each worker is processing, prevent duplicate work, and make status visible centrally.

## Context

This is a generalized account of professional engineering work. Employer identity, vendor/product names, location counts, infrastructure identifiers, internal schemas, schedules, credentials, and proprietary processing formats are intentionally omitted.

The system is currently in development/integration. The core application-automation path has been tested: terminate the existing application process when necessary, configure it for the target location, launch it, generate that location's price-book output, and repeat through locations in a loop.

The VM Manager/orchestration layer is the next major test boundary and has **not** yet been characterized as proven. Its testing follows finalization of the worker VM specification.

## Architecture / Approach

The public architecture can be represented as:

**Central Job Queue / History → VM Manager → Fleet of Worker VMs → Existing Location Application → Store-equivalent Price Book Output**

| Responsibility | Generalized role |
| --- | --- |
| Central job/history | Record location-scoped work, claims, state, and operational history |
| VM Manager | Coordinate worker infrastructure and the work that needs attention |
| Worker VM | Claim and execute location-specific work |
| Existing application automation | Configure and run the same application path used at a location |
| Output | Produce the equivalent location-specific price-book result |

Atomic claiming and duplicate prevention are used at the job-coordination boundary. They should not be described as an end-to-end exactly-once guarantee.

The important design boundary is that orchestration and execution remain separate. The VM Manager coordinates infrastructure and workload; workers perform the location-specific application process; central history provides operational visibility.

## Decisions & Tradeoffs

**Centralize without rewriting the vendor workflow.** The architecture exists because waiting for a vendor change was not fast enough for the business need. Instead of replacing the existing application or inventing a different price-book-generation path, the worker fleet reproduces centrally what a store would already do.

That choice preserves the existing application behavior but introduces infrastructure and orchestration work: worker VM specifications, lifecycle management, job claiming, failure handling, and visibility all become responsibilities of the surrounding system.

**Separate orchestration from execution.** Keeping the VM Manager separate from the workers allows the infrastructure strategy to evolve without embedding VM lifecycle concerns into the store-equivalent execution path.

## Result / Current State

The core store-equivalent automation loop has been tested successfully: the application can be killed/configured/launched for a target location, generate the price book, and repeat through locations in a loop.

The complete distributed system is not being described as production-deployed. The next milestone is to finalize the VM specification and test the VM Manager against the worker fleet. No throughput, uptime, time-savings, or production-scale claims are made here.

A sanitized architecture diagram using the generalized components above is approved for the public case study.

## Lessons

A distributed architecture can be a compatibility strategy, not just a scaling strategy. In this case, the useful move was not to redesign the vendor application's business behavior; it was to reproduce the known location-side process centrally and build orchestration around it.

That also makes test boundaries important. A successful application-automation loop demonstrates the execution path, but it does not prove the VM-management layer or the complete distributed system. Keeping those claims separate makes the current state easier to reason about and communicate.
