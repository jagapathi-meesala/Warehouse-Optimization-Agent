# Rules

1. Reject missing, malformed, negative, or type-incompatible numeric inputs where the domain requires non-negative values.
2. Never invent inventory, demand, capacity, lead-time, or sensor data.
3. Keep calculations deterministic and explain the applied method in outputs.
4. Do not execute external warehouse actions; outputs are recommendations or calculations.
5. Never log or embed secrets in source code.
6. Runtime configuration must come from environment variables.
