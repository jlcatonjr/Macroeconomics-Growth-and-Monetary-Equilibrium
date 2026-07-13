<!-- AGENTTEAMS:BEGIN content v=1 -->
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
9. **Every request must generate a plan** — any request involving two or more implementation steps (steps that write, create, rename, delete, or make agent decisions) must produce: (a) a summary saved to `tmp/<plan-slug>.plan.md` and (b) a step-by-step CSV saved to `tmp/<plan-slug>.steps.csv` before the first step executes; the CSV must include columns: `step`, `agent`, `action`, `inputs`, `outputs`, `status`, `notes`; initial `status` for all rows is `pending`; after each step completes, pass remaining steps through `@adversarial` and `@conflict-auditor` before proceeding; create `tmp/` if it does not exist

---

## Source Repositories

- Project source files (read-only)

---

## Style Rules

No project-specific style rules defined.
<!-- AGENTTEAMS:END content -->

<!-- AGENTTEAMS:BEGIN project_overview v=1 -->
## Project Overview

**Name:** MacroeconomicsGrowthMonetaryEquilibrium
**Goal:** Produce an interactive Jupyter notebook textbook for macroeconomics, economic growth, and monetary equilibrium, covering 11 core chapters and graduate-level advanced content with real-world data homework assignments and interactive ipywidgets visualizations.
**Deliverable type:** CSV
**Output format:** Jupyter notebooks (.ipynb) with interactive widgets
<!-- AGENTTEAMS:END project_overview -->

<!-- AGENTTEAMS:BEGIN directory_structure v=1 -->
## Directory Structure

| Path | Purpose |
|------|---------|
| `.` | Primary authored deliverables |
| `build/` | Compiled/converted output artifacts |
| `figures/` | Diagrams and figures |
| `N/A — no citation database configured for this project` | Reference/bibliography database |
| `.github/agents/` | Agent definition files |
| `.github/agents/references/` | Shared reference data |
<!-- AGENTTEAMS:END directory_structure -->

<!-- AGENTTEAMS:BEGIN output_conventions v=1 -->
## Output Conventions

- All primary deliverables are authored in `.` as `HTML`
- Compiled output lives in `build/` and is **never edited directly**
- Figures are generated from source files in `figures/` — source files are authoritative
- Every deliverable must correspond to a Component Spec defined by a workstream expert
- Work summaries are authored in `workSummaries/` from canonical `tmp/by-week/` plan artifacts, legacy `tmp/` fallbacks, and git history
<!-- AGENTTEAMS:END output_conventions -->

<!-- AGENTTEAMS:BEGIN agent_team v=1 -->
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
- `@repo-liaison` — cross-repository impact tracking and coordination
- `@git-operations` — git/github operations and merge strategy workflow

### Domain Agents
- `@work-summarizer` — synthesizes daily/weekly/monthly work summaries from plan artifacts and git history
- `@primary-producer` — drafts and revises primary deliverables
- `@quality-auditor` — read-only structural and prose quality audit
- `@cohesion-repairer` — repairs within-section cohesion failures
- `@style-guardian` — enforces voice and style fidelity
- `@technical-validator` — verifies technical accuracy against authority sources
- `@output-compiler` — assembles components into the final deliverable package
- `@visual-designer` — creates and revises diagrams and figures
- `@tool-doc-researcher` — specialized domain agent

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
<!-- AGENTTEAMS:END agent_team -->

<!-- AGENTTEAMS:BEGIN tone_and_style v=1 -->
## Tone and Style

Default to terse output for read-only auditor and governance roles
(`@security`, `@adversarial`, `@code-hygiene`, `@conflict-auditor`,
`@navigator`, `@quality-auditor`, `@technical-validator`,
`@post-production-auditor`, `@module-doc-validator`,
`@reference-manager` in read mode): respond in ≤200 words unless
the task requires longer output. Producing roles
(`@primary-producer`, `@module-doc-author`, `@content-enricher`,
`@output-compiler`, `@orchestrator` when summarizing a multi-step
session) emit the deliverable in full and are exempt from this
default.

Terse mode reduces consumer-harness token consumption on the
common case of audit-and-route turns. Producing roles override the
default explicitly by saying so in their first line.
<!-- AGENTTEAMS:END tone_and_style -->

<!-- AGENTTEAMS:BEGIN authority_hierarchy v=1 -->
## Authority Hierarchy

1. **Project source files** — ground truth for all technical claims
<!-- AGENTTEAMS:END authority_hierarchy -->

<!-- AGENTTEAMS:BEGIN source_repositories v=1 -->
## Source Repositories

- Project source files (read-only)
<!-- AGENTTEAMS:END source_repositories -->
