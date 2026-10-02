# Explainability

## Inputs and Data Sources
The agent accepts structured JSON-like inputs supplied by an authorized caller, such as SKU demand, unit cost, pick rate, item cube, lead time, demand variability, and warehouse volume. Data sources are external to the core agent; the implementation uses only the fields supplied in each request and does not silently fetch or invent operational data.

### Input Requirements
Each tool validates required fields and basic types before calculation. Numeric fields are checked for domain-safe ranges, and malformed records are rejected with structured errors.

### Failure Handling
A missing field, invalid type, empty collection, or unsafe numeric value produces an error result rather than a fabricated operational value. Tool execution exceptions are converted into structured error objects.

## Decision and Reasoning
Inventory analysis ranks items by annual usage value, computes cumulative contribution, and assigns A/B/C classes using explicit cumulative-value bands. Slotting uses pick velocity as picks per day divided by item cube, while replenishment uses average demand, lead time, demand standard deviation, and a service-level z value to calculate safety stock and reorder point.

### Rules Applied
For ABC classification, items are ordered by annual usage value and the class is assigned from cumulative contribution before the current item crosses the 80 percent and 95 percent boundaries, so a dominant first item remains class A. The next class boundary is 95 percent, with the remainder assigned class C. Slotting maps pick velocity to forward-pick, standard-pick, or reserve zones using explicit pick-rate thresholds, and capacity maps utilization to available, moderate, high, or over-capacity status.

### Expected Outputs
Outputs are structured dictionaries containing calculated metrics, classifications, recommendations, or status fields. Results are deterministic for identical inputs and do not imply that a physical warehouse action has occurred.

### Worked Example
For replenishment, the calculation is safety stock = z × daily demand standard deviation × square root of lead time, followed by reorder point = average daily demand × lead time + safety stock. For capacity, usable capacity is total volume multiplied by the usable ratio, and utilization is used volume divided by usable capacity.

## Limits and Constraints
The agent cannot verify whether supplied warehouse data is current, complete, or physically accurate, and it does not connect to a live warehouse management system. It also does not model every operational constraint, so recommendations require human or system validation before execution.

### Constraints
The replenishment z mapping uses a small deterministic service-level table and caps unknown higher service levels at the highest supported value. Slotting thresholds are generic decision rules rather than site-specific optimization, and capacity analysis treats volume as the limiting resource rather than aisle, weight, pallet-position, or labor constraints.

### Known Issues
The core implementation has no live telemetry ingestion, historical forecasting model, route optimization, or stochastic simulation. It also cannot infer missing dimensions or demand history from SKU names.

### Unsupported Behavior
The agent does not place orders, move stock, reserve warehouse locations in a WMS, or modify external systems. It does not claim framework-specific execution compatibility without an external integration being separately implemented and tested.
