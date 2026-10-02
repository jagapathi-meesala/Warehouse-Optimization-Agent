"""Inventory health and ABC classification."""
from contracts.tool_contract import ToolContract, ToolMetadata

SCHEMA = {"type": "object", "required": ["items"], "properties": {"items": {"type": "array"}}}

def _execute(payload: dict) -> dict:
    items = payload["items"]
    if not isinstance(items, list) or not items:
        raise ValueError("items must be a non-empty list")
    if len(items) > 10000:
        raise ValueError("too many items")
    rows = []
    for item in items:
        if not isinstance(item, dict):
            raise ValueError("each item must be an object")
        sku = item.get("sku")
        demand = item.get("annual_demand")
        unit_cost = item.get("unit_cost")
        stock = item.get("current_stock")
        if not isinstance(sku, str) or not sku.strip(): raise ValueError("sku must be a non-empty string")
        if any(not isinstance(v, (int, float)) or isinstance(v, bool) or v < 0 for v in (demand, unit_cost, stock)):
            raise ValueError("annual_demand, unit_cost, and current_stock must be non-negative numbers")
        rows.append({"sku": sku, "annual_usage_value": demand * unit_cost, "current_stock": stock, "annual_demand": demand})
    rows.sort(key=lambda x: x["annual_usage_value"], reverse=True)
    total = sum(r["annual_usage_value"] for r in rows)
    cumulative = 0.0
    result = []
    for r in rows:
        prior_share = (cumulative / total) if total else 0.0
        cumulative += r["annual_usage_value"]
        share = (r["annual_usage_value"] / total) if total else 0.0
        cum_share = (cumulative / total) if total else 0.0
        abc = "A" if prior_share < 0.80 else ("B" if prior_share < 0.95 else "C")
        result.append({**r, "usage_value_share": round(share, 6), "cumulative_share": round(cum_share, 6), "abc_class": abc})
    return {"item_count": len(result), "total_annual_usage_value": round(total, 4), "items": result}

TOOL = ToolContract(ToolMetadata("analyze-inventory", "Classify inventory by annual usage value and report stock context.", SCHEMA), _execute)
