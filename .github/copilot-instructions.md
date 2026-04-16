# MacroeconomicsGrowthMonetaryEquilibrium — Copilot Instructions

> This file defines the conventions, authority hierarchy, and agent team structure for all GitHub Copilot agents in MacroeconomicsGrowthMonetaryEquilibrium.

---

## Project Overview

**Name:** MacroeconomicsGrowthMonetaryEquilibrium
**Goal:** Produce an interactive Jupyter notebook textbook for macroeconomics, economic growth, and monetary equilibrium, covering 11 core chapters and graduate-level advanced content with real-world data homework assignments and interactive ipywidgets visualizations.
**Deliverable type:** HTML
**Output format:** Jupyter notebooks (.ipynb) with interactive widgets

---

## Directory Structure

| Path | Purpose |
|------|---------|
| `.` | Primary authored deliverables |
| `build/` | Compiled/converted output artifacts |
| `figures/` | Diagrams and figures |
| `N/A — no citation database configured for this project` | Reference/bibliography database |
| `.github/agents/` | Agent definition files |
| `.github/agents/references/` | Shared reference data |

---

## Output Conventions

- All primary deliverables are authored in `.` as `HTML`
- Compiled output lives in `build/` and is **never edited directly**
- Figures are generated from source files in `figures/` — source files are authoritative
- Every deliverable must correspond to a Component Spec defined by a workstream expert

---

## Agent Team

### Orchestrator
- `@orchestrator` — coordinates all agents; entry point for all user requests

### Governance Agents
- `@navigator` — project structure and file location
- `@security` — destructive operation clearance
- `@code-hygiene` — architecture enforcement and anti-sprawl auditor
- `@adversarial` — presupposition critic
- `@conflict-auditor` — consistency enforcement
- `@conflict-resolution` — ACCEPT/REJECT/REVISE decisions on flagged conflicts
- `@cleanup` — artifact removal
- `@agent-updater` — documentation synchronization
- `@agent-refactor` — spec compliance and reference extraction

### Domain Agents
- `@primary-producer` — drafts and revises primary deliverables
- `@quality-auditor` — read-only structural and prose quality audit
- `@cohesion-repairer` — repairs within-section cohesion failures
- `@style-guardian` — enforces voice and style fidelity
- `@technical-validator` — verifies technical accuracy against authority sources
- `@output-compiler` — assembles components into the final deliverable package
- `@visual-designer` — creates and revises diagrams and figures

### Workstream Experts
- `@ch1-purposive-action-expert` — Chapter 1 - Purposive Action
- `@ch2-entrepreneurship-supply-demand-expert` — Chapter 2 - Entrepreneurship and Supply and Demand
- `@ch3-elements-macroeconomics-expert` — Chapter 3 - The Elements of Macroeconomics
- `@ch4-aggregate-supply-growth-expert` — Chapter 4 - Aggregate Supply, Technology, and Economic Growth
- `@ch5-money-expert` — Chapter 5 - Money
- `@ch6-aggregate-demand-expert` — Chapter 6 - Aggregate Demand
- `@ch7-monetary-dynamics-expert` — Chapter 7 - Monetary Dynamics and Aggregate Analysis
- `@ch8-money-credit-loanable-funds-expert` — Chapter 8 - Money and Credit - The Loanable Funds Market
- `@ch9-is-lm-expert` — Chapter 9 - IS-LM
- `@ch10-labor-expert` — Chapter 10 - Labor
- `@ch11-central-banking-expert` — Chapter 11 - Central Banking
- `@advanced-macroeconomics-expert` — Advanced Macroeconomics Course Notes
- `@data-homework-expert` — Data Homework Assignments

---

## Authority Hierarchy

1. **Project source files** — ground truth for all technical claims

---

## Constitutional Rules

1. **Security first** — destructive operations require `@security` clearance
2. **Code hygiene second** — code changes require `@code-hygiene` audit before merge
3. **Authority hierarchy is ground truth** — no agent may contradict a higher-authority source
4. **Primary deliverables are the canonical output** — build artifacts are derived, never primary
5. **No fabricated references** — every citation must be verifiable in `N/A — no citation database configured for this project`
6. **Voice fidelity** — `@style-guardian` is the sole arbiter of voice deviation rulings
7. **Living documentation** — agent docs must not accumulate stale content
8. **Always close with `@conflict-auditor`** — required after any multi-file change session

---

## Source Repositories

- Project source files (read-only)

---

## Style Rules

No project-specific style rules defined.
