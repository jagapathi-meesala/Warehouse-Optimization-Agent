---
name: inventory-analysis
description: Warehouse optimization capability for inventory-analysis.
---

# Inventory Analysis Skill

## Purpose
Classify inventory using annual usage value and identify the relative contribution of each SKU.

## Inputs
A list of SKU records containing annual demand, unit cost, and current stock.

## Processing
Annual usage value is annual demand multiplied by unit cost. Records are sorted by value and assigned ABC classes from cumulative contribution.

## Outputs
Return per-SKU usage value, contribution shares, cumulative share, and ABC class.

## Limitations
This is a value-based ABC method and does not incorporate service criticality, lead-time risk, or demand intermittency unless represented in additional tooling.

## Expected Behavior
Invalid records are rejected and no missing values are invented.
