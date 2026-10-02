"""Reorder point and safety stock calculation."""
from contracts.tool_contract import ToolContract, ToolMetadata
import math
SCHEMA = {"type": "object", "required": ["average_daily_demand", "lead_time_days", "demand_stddev_daily", "service_level"], "properties": {}}

def _execute(payload: dict) -> dict:
    vals = [payload.get(k) for k in ("average_daily_demand", "lead_time_days", "demand_stddev_daily", "service_level")]
    if any(not isinstance(v,(int,float)) or isinstance(v,bool) for v in vals): raise ValueError("all inputs must be numeric")
    avg, lead, std, service = vals
    if avg < 0 or lead <= 0 or std < 0 or not 0 < service < 1: raise ValueError("invalid replenishment inputs")
    z_table = [(0.90,1.282),(0.95,1.645),(0.975,1.96),(0.99,2.326),(0.999,3.09)]
    z = next((z for level,z in z_table if service <= level), 3.09)
    safety = z * std * math.sqrt(lead)
    rop = avg * lead + safety
    return {"z_value": z, "safety_stock": round(safety, 4), "reorder_point": round(rop, 4), "method": "continuous-review safety stock using daily demand deviation"}

TOOL = ToolContract(ToolMetadata("calculate-replenishment", "Calculate safety stock and reorder point from demand variability and lead time.", SCHEMA), _execute)
