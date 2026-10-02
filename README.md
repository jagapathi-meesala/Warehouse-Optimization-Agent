# Warehouse Optimization Agent

A framework-independent OpenGAP 0.1.0 agent for structured warehouse optimization analysis.

## Purpose
The agent supports four operational tasks: inventory ABC analysis, storage-zone slotting, replenishment calculations, and warehouse capacity assessment.

## Architecture
`agent.yaml` defines the portable manifest. `core/agent_core.py` dynamically discovers tools implementing `ToolContract`. `adapters/` exposes a framework-neutral adapter boundary, while `config/` reads runtime settings from environment variables.

## Installation
Use Python 3.11+ and install `requirements.txt` in an isolated environment.

## Configuration
Copy `.env.example` to a runtime environment and provide every variable listed there. No API keys or credentials are required by the core implementation.

## Tools
- `analyze-inventory`: annual usage-value ABC classification.
- `recommend-slotting`: pick-velocity storage-zone recommendation.
- `calculate-replenishment`: safety stock and reorder point.
- `assess-capacity`: usable volume and utilization assessment.

## Skills
The repository documents inventory analysis, warehouse slotting, replenishment planning, and capacity optimization skills.

## Usage
Instantiate `core.agent_core.AgentCore`, then call `execute(tool_name, payload)`. The result is a `ToolResult` with `ok`, `data`, or `error`.

## Testing
Run `pytest -q` and `python verification/readiness_audit.py` from the repository root.

## Portability
The core contract is framework-independent. The adapter layer can be wrapped by OpenAI SDK, CrewAI, Claude Code, or Lyzr integrations, but this repository does not claim those external runtimes are installed or end-to-end tested.

## Limitations
Recommendations use supplied structured data and explicit deterministic formulas. They do not account for every warehouse constraint such as aisle geometry, labor schedules, congestion, hazardous-material rules, or live WMS state unless those variables are supplied and modeled.
