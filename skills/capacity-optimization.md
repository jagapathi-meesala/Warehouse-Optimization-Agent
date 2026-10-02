# Capacity Optimization Skill

## Purpose
Assess warehouse usable volume and utilization.

## Inputs
Used volume, total volume, and usable-volume ratio.

## Processing
Usable capacity equals total volume multiplied by usable ratio. Utilization equals used volume divided by usable capacity.

## Outputs
Return usable capacity, utilization, status, and remaining capacity.

## Limitations
Volume is treated as the capacity constraint and does not represent pallet positions, floor loading, weight, fire-code constraints, or aisle access.

## Expected Behavior
Invalid ratios, negative used volume, and non-positive total volume are rejected.
