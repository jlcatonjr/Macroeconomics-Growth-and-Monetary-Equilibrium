<!-- AGENTTEAMS:BEGIN content v=1 -->
# MacroeconomicsGrowthMonetaryEquilibrium — Agent Team Topology

> **Auto-generated.** Regenerated on every `build_team.py` run.
> Do not edit manually — changes will be overwritten.

---

## Team Topology Graph

![MacroeconomicsGrowthMonetaryEquilibrium agent team topology](pipeline-graph.svg)

The handoff-only control-flow backbone (agents-list edges omitted):

![MacroeconomicsGrowthMonetaryEquilibrium handoff backbone](pipeline-handoffs.svg)

---

## Node Legend

| Colour | Agent Type |
| --- | --- |
| <svg width="12" height="12"><rect width="12" height="12" fill="#e8e8ff" stroke="#6666cc"/></svg> Blue-lavender | Governance |
| <svg width="12" height="12"><rect width="12" height="12" fill="#e8ffe8" stroke="#66aa66"/></svg> Green | Domain |
| <svg width="12" height="12"><rect width="12" height="12" fill="#fff8e8" stroke="#ccaa44"/></svg> Yellow | Workstream Expert |
| <svg width="12" height="12"><rect width="12" height="12" fill="#ffe8e8" stroke="#cc6666"/></svg> Red-pink | Tool Specialist |

---

## Agent Roster

| Agent | Type | User-Invokable | Tools |
| --- | --- | --- | --- |
| `advanced-macroeconomics-expert` | workstream_expert | No | read, search, agent |
| `adversarial` | governance | Yes | read, search |
| `agent-refactor` | governance | No | edit, search, agent |
| `agent-updater` | governance | No | edit, search, execute, agent |
| `ch1-purposive-action-expert` | workstream_expert | No | read, search, agent |
| `ch10-labor-expert` | workstream_expert | No | read, search, agent |
| `ch11-central-banking-expert` | workstream_expert | No | read, search, agent |
| `ch2-entrepreneurship-supply-demand-expert` | workstream_expert | No | read, search, agent |
| `ch3-elements-macroeconomics-expert` | workstream_expert | No | read, search, agent |
| `ch4-aggregate-supply-growth-expert` | workstream_expert | No | read, search, agent |
| `ch5-money-expert` | workstream_expert | No | read, search, agent |
| `ch6-aggregate-demand-expert` | workstream_expert | No | read, search, agent |
| `ch7-monetary-dynamics-expert` | workstream_expert | No | read, search, agent |
| `ch8-money-credit-loanable-funds-expert` | workstream_expert | No | read, search, agent |
| `ch9-is-lm-expert` | workstream_expert | No | read, search, agent |
| `cleanup` | governance | No | edit, search, execute |
| `code-hygiene` | governance | No | read, search |
| `cohesion-repairer` | domain | No | read, edit |
| `conflict-auditor` | governance | No | read, search |
| `conflict-resolution` | governance | No | edit, search, read |
| `content-enricher` | domain | Yes | read, edit, search |
| `data-homework-expert` | workstream_expert | No | read, search, agent |
| `git-operations` | governance | Yes | read, execute, search |
| `navigator` | governance | No | read, search, execute |
| `orchestrator` | governance | Yes | read, edit, search, execute, todo, agent |
| `output-compiler` | domain | No | read, edit, execute |
| `primary-producer` | domain | No | read, edit, search |
| `quality-auditor` | domain | No | read, search |
| `repo-liaison` | governance | No | read, edit, search, execute, agent |
| `security` | governance | No | read, search |
| `style-guardian` | domain | No | read, edit, search |
| `team-builder` | governance | Yes | read, edit, search, execute, todo |
| `technical-validator` | domain | No | read, search |
| `tool-doc-researcher` | tool_specialist | No | read, search |
| `visual-designer` | domain | No | read, edit, execute, search |
| `work-summarizer` | domain | Yes | read, search, execute, edit, agent |

---

## Adjacency List

| Agent | Receives from | Hands off to |
| --- | --- | --- |
| `advanced-macroeconomics-expert` | — | `adversarial`, `primary-producer` |
| `adversarial` | `advanced-macroeconomics-expert`, `ch1-purposive-action-expert`, `ch10-labor-expert`, `ch11-central-banking-expert`, `ch2-entrepreneurship-supply-demand-expert`, `ch3-elements-macroeconomics-expert`, `ch4-aggregate-supply-growth-expert`, `ch5-money-expert`, `ch6-aggregate-demand-expert`, `ch7-monetary-dynamics-expert`, `ch8-money-credit-loanable-funds-expert`, `ch9-is-lm-expert`, `data-homework-expert`, `work-summarizer` | — |
| `agent-refactor` | `agent-updater` | `conflict-auditor` |
| `agent-updater` | `conflict-auditor`, `tool-doc-researcher` | `agent-refactor`, `conflict-auditor` |
| `ch1-purposive-action-expert` | — | `adversarial`, `primary-producer` |
| `ch10-labor-expert` | — | `adversarial`, `primary-producer` |
| `ch11-central-banking-expert` | — | `adversarial`, `primary-producer` |
| `ch2-entrepreneurship-supply-demand-expert` | — | `adversarial`, `primary-producer` |
| `ch3-elements-macroeconomics-expert` | — | `adversarial`, `primary-producer` |
| `ch4-aggregate-supply-growth-expert` | — | `adversarial`, `primary-producer` |
| `ch5-money-expert` | — | `adversarial`, `primary-producer` |
| `ch6-aggregate-demand-expert` | — | `adversarial`, `primary-producer` |
| `ch7-monetary-dynamics-expert` | — | `adversarial`, `primary-producer` |
| `ch8-money-credit-loanable-funds-expert` | — | `adversarial`, `primary-producer` |
| `ch9-is-lm-expert` | — | `adversarial`, `primary-producer` |
| `cleanup` | — | — |
| `code-hygiene` | — | — |
| `cohesion-repairer` | `primary-producer`, `quality-auditor` | `quality-auditor`, `style-guardian` |
| `conflict-auditor` | `agent-refactor`, `agent-updater`, `primary-producer`, `technical-validator`, `work-summarizer` | `agent-updater`, `conflict-resolution`, `technical-validator` |
| `conflict-resolution` | `conflict-auditor` | — |
| `content-enricher` | — | `primary-producer`, `technical-validator` |
| `data-homework-expert` | — | `adversarial`, `primary-producer` |
| `git-operations` | — | — |
| `navigator` | — | — |
| `orchestrator` | `tool-doc-researcher` | — |
| `output-compiler` | — | `technical-validator` |
| `primary-producer` | `advanced-macroeconomics-expert`, `ch1-purposive-action-expert`, `ch10-labor-expert`, `ch11-central-banking-expert`, `ch2-entrepreneurship-supply-demand-expert`, `ch3-elements-macroeconomics-expert`, `ch4-aggregate-supply-growth-expert`, `ch5-money-expert`, `ch6-aggregate-demand-expert`, `ch7-monetary-dynamics-expert`, `ch8-money-credit-loanable-funds-expert`, `ch9-is-lm-expert`, `content-enricher`, `data-homework-expert`, `quality-auditor`, `style-guardian`, `technical-validator` | `cohesion-repairer`, `conflict-auditor`, `quality-auditor`, `style-guardian` |
| `quality-auditor` | `cohesion-repairer`, `primary-producer`, `visual-designer` | `cohesion-repairer`, `primary-producer`, `style-guardian` |
| `repo-liaison` | — | — |
| `security` | — | — |
| `style-guardian` | `cohesion-repairer`, `primary-producer`, `quality-auditor` | `primary-producer` |
| `team-builder` | — | — |
| `technical-validator` | `conflict-auditor`, `content-enricher`, `output-compiler`, `work-summarizer` | `conflict-auditor`, `primary-producer` |
| `tool-doc-researcher` | — | `agent-updater`, `orchestrator` |
| `visual-designer` | — | `quality-auditor` |
| `work-summarizer` | — | `adversarial`, `conflict-auditor`, `technical-validator` |

---

## Diagram Source

<details>
<summary>Mermaid &amp; DOT source for the topology diagram above</summary>

```mermaid
flowchart LR
    classDef governance fill:#e8e8ff,stroke:#6666cc,color:#000
    classDef domain    fill:#e8ffe8,stroke:#66aa66,color:#000
    classDef workstream_expert fill:#fff8e8,stroke:#ccaa44,color:#000
    classDef tool_specialist   fill:#ffe8e8,stroke:#cc6666,color:#000
    classDef unknown   fill:#f5f5f5,stroke:#999,color:#000
    advanced_macroeconomics_expert["Advanced Macroeconomics Course Notes Expert"]
    class advanced_macroeconomics_expert workstream_expert
    adversarial["Adversarial"]
    class adversarial governance
    agent_refactor["Agent Refactor"]
    class agent_refactor governance
    agent_updater["Agent Updater"]
    class agent_updater governance
    ch1_purposive_action_expert["Chapter 1 - Purposive Action Expert"]
    class ch1_purposive_action_expert workstream_expert
    ch10_labor_expert["Chapter 10 - Labor Expert"]
    class ch10_labor_expert workstream_expert
    ch11_central_banking_expert["Chapter 11 - Central Banking Expert"]
    class ch11_central_banking_expert workstream_expert
    ch2_entrepreneurship_supply_demand_expert["Chapter 2 - Entrepreneurship and Supply and Demand Expert"]
    class ch2_entrepreneurship_supply_demand_expert workstream_expert
    ch3_elements_macroeconomics_expert["Chapter 3 - The Elements of Macroeconomics Expert"]
    class ch3_elements_macroeconomics_expert workstream_expert
    ch4_aggregate_supply_growth_expert["Chapter 4 - Aggregate Supply, Technology, and Economic Growth Expert"]
    class ch4_aggregate_supply_growth_expert workstream_expert
    ch5_money_expert["Chapter 5 - Money Expert"]
    class ch5_money_expert workstream_expert
    ch6_aggregate_demand_expert["Chapter 6 - Aggregate Demand Expert"]
    class ch6_aggregate_demand_expert workstream_expert
    ch7_monetary_dynamics_expert["Chapter 7 - Monetary Dynamics and Aggregate Analysis Expert"]
    class ch7_monetary_dynamics_expert workstream_expert
    ch8_money_credit_loanable_funds_expert["Chapter 8 - Money and Credit - The Loanable Funds Market Expert"]
    class ch8_money_credit_loanable_funds_expert workstream_expert
    ch9_is_lm_expert["Chapter 9 - IS-LM Expert"]
    class ch9_is_lm_expert workstream_expert
    cleanup["Cleanup"]
    class cleanup governance
    code_hygiene["Code Hygiene"]
    class code_hygiene governance
    cohesion_repairer["Cohesion Repairer"]
    class cohesion_repairer domain
    conflict_auditor["Conflict Auditor"]
    class conflict_auditor governance
    conflict_resolution["Conflict Resolution"]
    class conflict_resolution governance
    content_enricher["Content Enricher"]
    class content_enricher domain
    data_homework_expert["Data Homework Assignments Expert"]
    class data_homework_expert workstream_expert
    git_operations["Git Operations"]
    class git_operations governance
    navigator["Navigator"]
    class navigator governance
    orchestrator["Orchestrator"]
    class orchestrator governance
    output_compiler["Output Compiler"]
    class output_compiler domain
    primary_producer["Primary Producer"]
    class primary_producer domain
    quality_auditor["Quality Auditor"]
    class quality_auditor domain
    repo_liaison["Repo Liaison"]
    class repo_liaison governance
    security["Security"]
    class security governance
    style_guardian["Style Guardian"]
    class style_guardian domain
    team_builder["Team Builder"]
    class team_builder governance
    technical_validator["Technical Validator"]
    class technical_validator domain
    tool_doc_researcher["Tool Documentation Researcher"]
    class tool_doc_researcher tool_specialist
    visual_designer["Visual Designer"]
    class visual_designer domain
    work_summarizer["Work Summarizer"]
    class work_summarizer domain
    advanced_macroeconomics_expert -.-> adversarial
    advanced_macroeconomics_expert -.-> primary_producer
    agent_refactor -.-> conflict_auditor
    agent_updater -.-> agent_refactor
    agent_updater -.-> conflict_auditor
    ch1_purposive_action_expert -.-> adversarial
    ch1_purposive_action_expert -.-> primary_producer
    ch10_labor_expert -.-> adversarial
    ch10_labor_expert -.-> primary_producer
    ch11_central_banking_expert -.-> adversarial
    ch11_central_banking_expert -.-> primary_producer
    ch2_entrepreneurship_supply_demand_expert -.-> adversarial
    ch2_entrepreneurship_supply_demand_expert -.-> primary_producer
    ch3_elements_macroeconomics_expert -.-> adversarial
    ch3_elements_macroeconomics_expert -.-> primary_producer
    ch4_aggregate_supply_growth_expert -.-> adversarial
    ch4_aggregate_supply_growth_expert -.-> primary_producer
    ch5_money_expert -.-> adversarial
    ch5_money_expert -.-> primary_producer
    ch6_aggregate_demand_expert -.-> adversarial
    ch6_aggregate_demand_expert -.-> primary_producer
    ch7_monetary_dynamics_expert -.-> adversarial
    ch7_monetary_dynamics_expert -.-> primary_producer
    ch8_money_credit_loanable_funds_expert -.-> adversarial
    ch8_money_credit_loanable_funds_expert -.-> primary_producer
    ch9_is_lm_expert -.-> adversarial
    ch9_is_lm_expert -.-> primary_producer
    cohesion_repairer -.-> quality_auditor
    cohesion_repairer -.-> style_guardian
    conflict_auditor -.-> agent_updater
    conflict_auditor -.-> conflict_resolution
    conflict_auditor -.-> technical_validator
    content_enricher -.-> primary_producer
    content_enricher -.-> technical_validator
    data_homework_expert -.-> adversarial
    data_homework_expert -.-> primary_producer
    output_compiler -.-> technical_validator
    primary_producer -.-> cohesion_repairer
    primary_producer -.-> conflict_auditor
    primary_producer -.-> quality_auditor
    primary_producer -.-> style_guardian
    quality_auditor -.-> cohesion_repairer
    quality_auditor -.-> primary_producer
    quality_auditor -.-> style_guardian
    style_guardian -.-> primary_producer
    technical_validator -.-> conflict_auditor
    technical_validator -.-> primary_producer
    tool_doc_researcher -->|"Update Brief and Generated Docs"| agent_updater
    tool_doc_researcher -->|"Return to Orchestrator"| orchestrator
    visual_designer -.-> quality_auditor
    work_summarizer -.-> adversarial
    work_summarizer -.-> conflict_auditor
    work_summarizer -.-> technical_validator
```

```dot
digraph "MacroeconomicsGrowthMonetaryEquilibrium Agent Team" {
    rankdir=LR;
    node [fontname="Helvetica", fontsize=11, shape=box, style="rounded,filled"];
    edge [fontsize=9];
    "advanced-macroeconomics-expert" [label="Advanced Macroeconomics Course Notes Expert", fillcolor="#fff8e8"];
    "adversarial" [label="Adversarial", fillcolor="#e8e8ff"];
    "agent-refactor" [label="Agent Refactor", fillcolor="#e8e8ff"];
    "agent-updater" [label="Agent Updater", fillcolor="#e8e8ff"];
    "ch1-purposive-action-expert" [label="Chapter 1 - Purposive Action Expert", fillcolor="#fff8e8"];
    "ch10-labor-expert" [label="Chapter 10 - Labor Expert", fillcolor="#fff8e8"];
    "ch11-central-banking-expert" [label="Chapter 11 - Central Banking Expert", fillcolor="#fff8e8"];
    "ch2-entrepreneurship-supply-demand-expert" [label="Chapter 2 - Entrepreneurship and Supply and Demand Expert", fillcolor="#fff8e8"];
    "ch3-elements-macroeconomics-expert" [label="Chapter 3 - The Elements of Macroeconomics Expert", fillcolor="#fff8e8"];
    "ch4-aggregate-supply-growth-expert" [label="Chapter 4 - Aggregate Supply, Technology, and Economic Growth Expert", fillcolor="#fff8e8"];
    "ch5-money-expert" [label="Chapter 5 - Money Expert", fillcolor="#fff8e8"];
    "ch6-aggregate-demand-expert" [label="Chapter 6 - Aggregate Demand Expert", fillcolor="#fff8e8"];
    "ch7-monetary-dynamics-expert" [label="Chapter 7 - Monetary Dynamics and Aggregate Analysis Expert", fillcolor="#fff8e8"];
    "ch8-money-credit-loanable-funds-expert" [label="Chapter 8 - Money and Credit - The Loanable Funds Market Expert", fillcolor="#fff8e8"];
    "ch9-is-lm-expert" [label="Chapter 9 - IS-LM Expert", fillcolor="#fff8e8"];
    "cleanup" [label="Cleanup", fillcolor="#e8e8ff"];
    "code-hygiene" [label="Code Hygiene", fillcolor="#e8e8ff"];
    "cohesion-repairer" [label="Cohesion Repairer", fillcolor="#e8ffe8"];
    "conflict-auditor" [label="Conflict Auditor", fillcolor="#e8e8ff"];
    "conflict-resolution" [label="Conflict Resolution", fillcolor="#e8e8ff"];
    "content-enricher" [label="Content Enricher", fillcolor="#e8ffe8"];
    "data-homework-expert" [label="Data Homework Assignments Expert", fillcolor="#fff8e8"];
    "git-operations" [label="Git Operations", fillcolor="#e8e8ff"];
    "navigator" [label="Navigator", fillcolor="#e8e8ff"];
    "orchestrator" [label="Orchestrator", fillcolor="#e8e8ff"];
    "output-compiler" [label="Output Compiler", fillcolor="#e8ffe8"];
    "primary-producer" [label="Primary Producer", fillcolor="#e8ffe8"];
    "quality-auditor" [label="Quality Auditor", fillcolor="#e8ffe8"];
    "repo-liaison" [label="Repo Liaison", fillcolor="#e8e8ff"];
    "security" [label="Security", fillcolor="#e8e8ff"];
    "style-guardian" [label="Style Guardian", fillcolor="#e8ffe8"];
    "team-builder" [label="Team Builder", fillcolor="#e8e8ff"];
    "technical-validator" [label="Technical Validator", fillcolor="#e8ffe8"];
    "tool-doc-researcher" [label="Tool Documentation Researcher", fillcolor="#ffe8e8"];
    "visual-designer" [label="Visual Designer", fillcolor="#e8ffe8"];
    "work-summarizer" [label="Work Summarizer", fillcolor="#e8ffe8"];
    "advanced-macroeconomics-expert" -> "adversarial" [style=dashed];
    "advanced-macroeconomics-expert" -> "primary-producer" [style=dashed];
    "agent-refactor" -> "conflict-auditor" [style=dashed];
    "agent-updater" -> "agent-refactor" [style=dashed];
    "agent-updater" -> "conflict-auditor" [style=dashed];
    "ch1-purposive-action-expert" -> "adversarial" [style=dashed];
    "ch1-purposive-action-expert" -> "primary-producer" [style=dashed];
    "ch10-labor-expert" -> "adversarial" [style=dashed];
    "ch10-labor-expert" -> "primary-producer" [style=dashed];
    "ch11-central-banking-expert" -> "adversarial" [style=dashed];
    "ch11-central-banking-expert" -> "primary-producer" [style=dashed];
    "ch2-entrepreneurship-supply-demand-expert" -> "adversarial" [style=dashed];
    "ch2-entrepreneurship-supply-demand-expert" -> "primary-producer" [style=dashed];
    "ch3-elements-macroeconomics-expert" -> "adversarial" [style=dashed];
    "ch3-elements-macroeconomics-expert" -> "primary-producer" [style=dashed];
    "ch4-aggregate-supply-growth-expert" -> "adversarial" [style=dashed];
    "ch4-aggregate-supply-growth-expert" -> "primary-producer" [style=dashed];
    "ch5-money-expert" -> "adversarial" [style=dashed];
    "ch5-money-expert" -> "primary-producer" [style=dashed];
    "ch6-aggregate-demand-expert" -> "adversarial" [style=dashed];
    "ch6-aggregate-demand-expert" -> "primary-producer" [style=dashed];
    "ch7-monetary-dynamics-expert" -> "adversarial" [style=dashed];
    "ch7-monetary-dynamics-expert" -> "primary-producer" [style=dashed];
    "ch8-money-credit-loanable-funds-expert" -> "adversarial" [style=dashed];
    "ch8-money-credit-loanable-funds-expert" -> "primary-producer" [style=dashed];
    "ch9-is-lm-expert" -> "adversarial" [style=dashed];
    "ch9-is-lm-expert" -> "primary-producer" [style=dashed];
    "cohesion-repairer" -> "quality-auditor" [style=dashed];
    "cohesion-repairer" -> "style-guardian" [style=dashed];
    "conflict-auditor" -> "agent-updater" [style=dashed];
    "conflict-auditor" -> "conflict-resolution" [style=dashed];
    "conflict-auditor" -> "technical-validator" [style=dashed];
    "content-enricher" -> "primary-producer" [style=dashed];
    "content-enricher" -> "technical-validator" [style=dashed];
    "data-homework-expert" -> "adversarial" [style=dashed];
    "data-homework-expert" -> "primary-producer" [style=dashed];
    "output-compiler" -> "technical-validator" [style=dashed];
    "primary-producer" -> "cohesion-repairer" [style=dashed];
    "primary-producer" -> "conflict-auditor" [style=dashed];
    "primary-producer" -> "quality-auditor" [style=dashed];
    "primary-producer" -> "style-guardian" [style=dashed];
    "quality-auditor" -> "cohesion-repairer" [style=dashed];
    "quality-auditor" -> "primary-producer" [style=dashed];
    "quality-auditor" -> "style-guardian" [style=dashed];
    "style-guardian" -> "primary-producer" [style=dashed];
    "technical-validator" -> "conflict-auditor" [style=dashed];
    "technical-validator" -> "primary-producer" [style=dashed];
    "tool-doc-researcher" -> "agent-updater" [style=solid, label="Update Brief and Generated Docs"];
    "tool-doc-researcher" -> "orchestrator" [style=solid, label="Return to Orchestrator"];
    "visual-designer" -> "quality-auditor" [style=dashed];
    "work-summarizer" -> "adversarial" [style=dashed];
    "work-summarizer" -> "conflict-auditor" [style=dashed];
    "work-summarizer" -> "technical-validator" [style=dashed];
}
```

</details>

---

## JSON Adjacency

```json
{
  "project_name": "MacroeconomicsGrowthMonetaryEquilibrium",
  "nodes": {
    "advanced-macroeconomics-expert": {
      "display_name": "Advanced Macroeconomics Course Notes Expert",
      "agent_type": "workstream_expert",
      "user_invokable": false,
      "tools": [
        "read",
        "search",
        "agent"
      ]
    },
    "adversarial": {
      "display_name": "Adversarial",
      "agent_type": "governance",
      "user_invokable": true,
      "tools": [
        "read",
        "search"
      ]
    },
    "agent-refactor": {
      "display_name": "Agent Refactor",
      "agent_type": "governance",
      "user_invokable": false,
      "tools": [
        "edit",
        "search",
        "agent"
      ]
    },
    "agent-updater": {
      "display_name": "Agent Updater",
      "agent_type": "governance",
      "user_invokable": false,
      "tools": [
        "edit",
        "search",
        "execute",
        "agent"
      ]
    },
    "ch1-purposive-action-expert": {
      "display_name": "Chapter 1 - Purposive Action Expert",
      "agent_type": "workstream_expert",
      "user_invokable": false,
      "tools": [
        "read",
        "search",
        "agent"
      ]
    },
    "ch10-labor-expert": {
      "display_name": "Chapter 10 - Labor Expert",
      "agent_type": "workstream_expert",
      "user_invokable": false,
      "tools": [
        "read",
        "search",
        "agent"
      ]
    },
    "ch11-central-banking-expert": {
      "display_name": "Chapter 11 - Central Banking Expert",
      "agent_type": "workstream_expert",
      "user_invokable": false,
      "tools": [
        "read",
        "search",
        "agent"
      ]
    },
    "ch2-entrepreneurship-supply-demand-expert": {
      "display_name": "Chapter 2 - Entrepreneurship and Supply and Demand Expert",
      "agent_type": "workstream_expert",
      "user_invokable": false,
      "tools": [
        "read",
        "search",
        "agent"
      ]
    },
    "ch3-elements-macroeconomics-expert": {
      "display_name": "Chapter 3 - The Elements of Macroeconomics Expert",
      "agent_type": "workstream_expert",
      "user_invokable": false,
      "tools": [
        "read",
        "search",
        "agent"
      ]
    },
    "ch4-aggregate-supply-growth-expert": {
      "display_name": "Chapter 4 - Aggregate Supply, Technology, and Economic Growth Expert",
      "agent_type": "workstream_expert",
      "user_invokable": false,
      "tools": [
        "read",
        "search",
        "agent"
      ]
    },
    "ch5-money-expert": {
      "display_name": "Chapter 5 - Money Expert",
      "agent_type": "workstream_expert",
      "user_invokable": false,
      "tools": [
        "read",
        "search",
        "agent"
      ]
    },
    "ch6-aggregate-demand-expert": {
      "display_name": "Chapter 6 - Aggregate Demand Expert",
      "agent_type": "workstream_expert",
      "user_invokable": false,
      "tools": [
        "read",
        "search",
        "agent"
      ]
    },
    "ch7-monetary-dynamics-expert": {
      "display_name": "Chapter 7 - Monetary Dynamics and Aggregate Analysis Expert",
      "agent_type": "workstream_expert",
      "user_invokable": false,
      "tools": [
        "read",
        "search",
        "agent"
      ]
    },
    "ch8-money-credit-loanable-funds-expert": {
      "display_name": "Chapter 8 - Money and Credit - The Loanable Funds Market Expert",
      "agent_type": "workstream_expert",
      "user_invokable": false,
      "tools": [
        "read",
        "search",
        "agent"
      ]
    },
    "ch9-is-lm-expert": {
      "display_name": "Chapter 9 - IS-LM Expert",
      "agent_type": "workstream_expert",
      "user_invokable": false,
      "tools": [
        "read",
        "search",
        "agent"
      ]
    },
    "cleanup": {
      "display_name": "Cleanup",
      "agent_type": "governance",
      "user_invokable": false,
      "tools": [
        "edit",
        "search",
        "execute"
      ]
    },
    "code-hygiene": {
      "display_name": "Code Hygiene",
      "agent_type": "governance",
      "user_invokable": false,
      "tools": [
        "read",
        "search"
      ]
    },
    "cohesion-repairer": {
      "display_name": "Cohesion Repairer",
      "agent_type": "domain",
      "user_invokable": false,
      "tools": [
        "read",
        "edit"
      ]
    },
    "conflict-auditor": {
      "display_name": "Conflict Auditor",
      "agent_type": "governance",
      "user_invokable": false,
      "tools": [
        "read",
        "search"
      ]
    },
    "conflict-resolution": {
      "display_name": "Conflict Resolution",
      "agent_type": "governance",
      "user_invokable": false,
      "tools": [
        "edit",
        "search",
        "read"
      ]
    },
    "content-enricher": {
      "display_name": "Content Enricher",
      "agent_type": "domain",
      "user_invokable": true,
      "tools": [
        "read",
        "edit",
        "search"
      ]
    },
    "data-homework-expert": {
      "display_name": "Data Homework Assignments Expert",
      "agent_type": "workstream_expert",
      "user_invokable": false,
      "tools": [
        "read",
        "search",
        "agent"
      ]
    },
    "git-operations": {
      "display_name": "Git Operations",
      "agent_type": "governance",
      "user_invokable": true,
      "tools": [
        "read",
        "execute",
        "search"
      ]
    },
    "navigator": {
      "display_name": "Navigator",
      "agent_type": "governance",
      "user_invokable": false,
      "tools": [
        "read",
        "search",
        "execute"
      ]
    },
    "orchestrator": {
      "display_name": "Orchestrator",
      "agent_type": "governance",
      "user_invokable": true,
      "tools": [
        "read",
        "edit",
        "search",
        "execute",
        "todo",
        "agent"
      ]
    },
    "output-compiler": {
      "display_name": "Output Compiler",
      "agent_type": "domain",
      "user_invokable": false,
      "tools": [
        "read",
        "edit",
        "execute"
      ]
    },
    "primary-producer": {
      "display_name": "Primary Producer",
      "agent_type": "domain",
      "user_invokable": false,
      "tools": [
        "read",
        "edit",
        "search"
      ]
    },
    "quality-auditor": {
      "display_name": "Quality Auditor",
      "agent_type": "domain",
      "user_invokable": false,
      "tools": [
        "read",
        "search"
      ]
    },
    "repo-liaison": {
      "display_name": "Repo Liaison",
      "agent_type": "governance",
      "user_invokable": false,
      "tools": [
        "read",
        "edit",
        "search",
        "execute",
        "agent"
      ]
    },
    "security": {
      "display_name": "Security",
      "agent_type": "governance",
      "user_invokable": false,
      "tools": [
        "read",
        "search"
      ]
    },
    "style-guardian": {
      "display_name": "Style Guardian",
      "agent_type": "domain",
      "user_invokable": false,
      "tools": [
        "read",
        "edit",
        "search"
      ]
    },
    "team-builder": {
      "display_name": "Team Builder",
      "agent_type": "governance",
      "user_invokable": true,
      "tools": [
        "read",
        "edit",
        "search",
        "execute",
        "todo"
      ]
    },
    "technical-validator": {
      "display_name": "Technical Validator",
      "agent_type": "domain",
      "user_invokable": false,
      "tools": [
        "read",
        "search"
      ]
    },
    "tool-doc-researcher": {
      "display_name": "Tool Documentation Researcher",
      "agent_type": "tool_specialist",
      "user_invokable": false,
      "tools": [
        "read",
        "search"
      ]
    },
    "visual-designer": {
      "display_name": "Visual Designer",
      "agent_type": "domain",
      "user_invokable": false,
      "tools": [
        "read",
        "edit",
        "execute",
        "search"
      ]
    },
    "work-summarizer": {
      "display_name": "Work Summarizer",
      "agent_type": "domain",
      "user_invokable": true,
      "tools": [
        "read",
        "search",
        "execute",
        "edit",
        "agent"
      ]
    }
  },
  "edges": [
    {
      "source": "advanced-macroeconomics-expert",
      "target": "adversarial",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "advanced-macroeconomics-expert",
      "target": "primary-producer",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "agent-refactor",
      "target": "conflict-auditor",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "agent-updater",
      "target": "agent-refactor",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "agent-updater",
      "target": "conflict-auditor",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "ch1-purposive-action-expert",
      "target": "adversarial",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "ch1-purposive-action-expert",
      "target": "primary-producer",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "ch10-labor-expert",
      "target": "adversarial",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "ch10-labor-expert",
      "target": "primary-producer",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "ch11-central-banking-expert",
      "target": "adversarial",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "ch11-central-banking-expert",
      "target": "primary-producer",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "ch2-entrepreneurship-supply-demand-expert",
      "target": "adversarial",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "ch2-entrepreneurship-supply-demand-expert",
      "target": "primary-producer",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "ch3-elements-macroeconomics-expert",
      "target": "adversarial",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "ch3-elements-macroeconomics-expert",
      "target": "primary-producer",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "ch4-aggregate-supply-growth-expert",
      "target": "adversarial",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "ch4-aggregate-supply-growth-expert",
      "target": "primary-producer",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "ch5-money-expert",
      "target": "adversarial",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "ch5-money-expert",
      "target": "primary-producer",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "ch6-aggregate-demand-expert",
      "target": "adversarial",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "ch6-aggregate-demand-expert",
      "target": "primary-producer",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "ch7-monetary-dynamics-expert",
      "target": "adversarial",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "ch7-monetary-dynamics-expert",
      "target": "primary-producer",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "ch8-money-credit-loanable-funds-expert",
      "target": "adversarial",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "ch8-money-credit-loanable-funds-expert",
      "target": "primary-producer",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "ch9-is-lm-expert",
      "target": "adversarial",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "ch9-is-lm-expert",
      "target": "primary-producer",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "cohesion-repairer",
      "target": "quality-auditor",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "cohesion-repairer",
      "target": "style-guardian",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "conflict-auditor",
      "target": "agent-updater",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "conflict-auditor",
      "target": "conflict-resolution",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "conflict-auditor",
      "target": "technical-validator",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "content-enricher",
      "target": "primary-producer",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "content-enricher",
      "target": "technical-validator",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "data-homework-expert",
      "target": "adversarial",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "data-homework-expert",
      "target": "primary-producer",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "output-compiler",
      "target": "technical-validator",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "primary-producer",
      "target": "cohesion-repairer",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "primary-producer",
      "target": "conflict-auditor",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "primary-producer",
      "target": "quality-auditor",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "primary-producer",
      "target": "style-guardian",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "quality-auditor",
      "target": "cohesion-repairer",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "quality-auditor",
      "target": "primary-producer",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "quality-auditor",
      "target": "style-guardian",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "style-guardian",
      "target": "primary-producer",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "technical-validator",
      "target": "conflict-auditor",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "technical-validator",
      "target": "primary-producer",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "tool-doc-researcher",
      "target": "agent-updater",
      "edge_type": "handoff",
      "label": "Update Brief and Generated Docs"
    },
    {
      "source": "tool-doc-researcher",
      "target": "orchestrator",
      "edge_type": "handoff",
      "label": "Return to Orchestrator"
    },
    {
      "source": "visual-designer",
      "target": "quality-auditor",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "work-summarizer",
      "target": "adversarial",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "work-summarizer",
      "target": "conflict-auditor",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "work-summarizer",
      "target": "technical-validator",
      "edge_type": "agents-list",
      "label": null
    }
  ],
  "adjacency": {
    "advanced-macroeconomics-expert": [
      "adversarial",
      "primary-producer"
    ],
    "adversarial": [],
    "agent-refactor": [
      "conflict-auditor"
    ],
    "agent-updater": [
      "agent-refactor",
      "conflict-auditor"
    ],
    "ch1-purposive-action-expert": [
      "adversarial",
      "primary-producer"
    ],
    "ch10-labor-expert": [
      "adversarial",
      "primary-producer"
    ],
    "ch11-central-banking-expert": [
      "adversarial",
      "primary-producer"
    ],
    "ch2-entrepreneurship-supply-demand-expert": [
      "adversarial",
      "primary-producer"
    ],
    "ch3-elements-macroeconomics-expert": [
      "adversarial",
      "primary-producer"
    ],
    "ch4-aggregate-supply-growth-expert": [
      "adversarial",
      "primary-producer"
    ],
    "ch5-money-expert": [
      "adversarial",
      "primary-producer"
    ],
    "ch6-aggregate-demand-expert": [
      "adversarial",
      "primary-producer"
    ],
    "ch7-monetary-dynamics-expert": [
      "adversarial",
      "primary-producer"
    ],
    "ch8-money-credit-loanable-funds-expert": [
      "adversarial",
      "primary-producer"
    ],
    "ch9-is-lm-expert": [
      "adversarial",
      "primary-producer"
    ],
    "cleanup": [],
    "code-hygiene": [],
    "cohesion-repairer": [
      "quality-auditor",
      "style-guardian"
    ],
    "conflict-auditor": [
      "agent-updater",
      "conflict-resolution",
      "technical-validator"
    ],
    "conflict-resolution": [],
    "content-enricher": [
      "primary-producer",
      "technical-validator"
    ],
    "data-homework-expert": [
      "adversarial",
      "primary-producer"
    ],
    "git-operations": [],
    "navigator": [],
    "orchestrator": [],
    "output-compiler": [
      "technical-validator"
    ],
    "primary-producer": [
      "cohesion-repairer",
      "conflict-auditor",
      "quality-auditor",
      "style-guardian"
    ],
    "quality-auditor": [
      "cohesion-repairer",
      "primary-producer",
      "style-guardian"
    ],
    "repo-liaison": [],
    "security": [],
    "style-guardian": [
      "primary-producer"
    ],
    "team-builder": [],
    "technical-validator": [
      "conflict-auditor",
      "primary-producer"
    ],
    "tool-doc-researcher": [
      "agent-updater",
      "orchestrator"
    ],
    "visual-designer": [
      "quality-auditor"
    ],
    "work-summarizer": [
      "adversarial",
      "conflict-auditor",
      "technical-validator"
    ]
  }
}
```
<!-- AGENTTEAMS:END content -->
