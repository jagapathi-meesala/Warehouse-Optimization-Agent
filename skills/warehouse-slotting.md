# Warehouse Slotting Skill

## Purpose
Recommend a storage zone based on pick velocity relative to item cube.

## Inputs
SKU, picks per day, and item cube in cubic meters.

## Processing
Velocity is calculated as picks per day divided by cube. The result is mapped to explicit storage-zone thresholds.

## Outputs
Return velocity index and recommended zone for each SKU.

## Limitations
The method does not model aisle geometry, travel distance, ergonomics, weight, hazard classes, or actual bin availability.

## Expected Behavior
The result is deterministic for identical inputs and is a recommendation, not a physical placement command.
