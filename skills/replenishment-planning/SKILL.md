---
name: replenishment-planning
description: Warehouse optimization capability for replenishment-planning.
---

# Replenishment Planning Skill

## Purpose
Calculate safety stock and reorder point from demand variability and lead time.

## Inputs
Average daily demand, lead time in days, daily demand standard deviation, and target service level.

## Processing
A deterministic z-value table is used. Safety stock and reorder point are then calculated from the documented formulas.

## Outputs
Return z value, safety stock, reorder point, and calculation method.

## Limitations
The method assumes independent daily demand variation and does not estimate forecast bias, supplier reliability, or order-cycle economics.

## Expected Behavior
Invalid service levels and non-positive lead times are rejected.
