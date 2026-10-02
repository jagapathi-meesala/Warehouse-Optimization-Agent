"""Deterministic warehouse slotting recommendation."""
from contracts.tool_contract import ToolContract, ToolMetadata
SCHEMA = {"type": "object", "required": ["items"], "properties": {"items": {"type": "array"}}}

def _execute(payload: dict) -> dict:
    items = payload["items"]
    if not isinstance(items, list) or not items: raise ValueError("items must be a non-empty list")
    ranked = []
    for x in items:
        if not isinstance(x, dict): raise ValueError("each item must be an object")
        sku, picks, cube = x.get("sku"), x.get("picks_per_day"), x.get("cube_m3")
        if not isinstance(sku, str) or not sku.strip(): raise ValueError("sku must be a non-empty string")
        if not isinstance(picks, (int,float)) or isinstance(picks,bool) or picks < 0: raise ValueError("picks_per_day must be non-negative")
        if not isinstance(cube, (int,float)) or isinstance(cube,bool) or cube <= 0: raise ValueError("cube_m3 must be positive")
        velocity = picks / cube
        zone = "forward-pick" if picks >= 20 else ("standard-pick" if picks >= 5 else "reserve")
        ranked.append({"sku": sku, "velocity_index": round(velocity, 4), "recommended_zone": zone, "picks_per_day": picks, "cube_m3": cube})
    ranked.sort(key=lambda x: x["velocity_index"], reverse=True)
    return {"recommendations": ranked}

TOOL = ToolContract(ToolMetadata("recommend-slotting", "Recommend storage zones from pick velocity and item cube.", SCHEMA), _execute)
