"""Warehouse capacity utilization assessment."""
from contracts.tool_contract import ToolContract, ToolMetadata
SCHEMA = {"type": "object", "required": ["used_volume_m3", "total_volume_m3", "usable_ratio"], "properties": {}}

def _execute(payload: dict) -> dict:
    used, total, ratio = payload.get("used_volume_m3"), payload.get("total_volume_m3"), payload.get("usable_ratio")
    if any(not isinstance(v,(int,float)) or isinstance(v,bool) for v in (used,total,ratio)): raise ValueError("capacity inputs must be numeric")
    if used < 0 or total <= 0 or not 0 < ratio <= 1: raise ValueError("invalid capacity inputs")
    usable = total * ratio
    utilization = used / usable
    status = "over-capacity" if utilization > 1 else ("high" if utilization >= 0.85 else ("moderate" if utilization >= 0.70 else "available"))
    return {"usable_capacity_m3": round(usable,4), "utilization": round(utilization,4), "status": status, "remaining_capacity_m3": round(max(0, usable-used),4)}

TOOL = ToolContract(ToolMetadata("assess-capacity", "Assess usable warehouse volume, utilization, and remaining capacity.", SCHEMA), _execute)
