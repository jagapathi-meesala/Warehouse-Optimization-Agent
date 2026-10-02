from tools.analyze_inventory import TOOL as inventory
from tools.recommend_slotting import TOOL as slotting
from tools.calculate_replenishment import TOOL as replenish
from tools.assess_capacity import TOOL as capacity

def test_inventory_abc():
    r=inventory.execute({"items":[{"sku":"A","annual_demand":100,"unit_cost":10,"current_stock":20},{"sku":"B","annual_demand":10,"unit_cost":1,"current_stock":5}]})
    assert r.ok and r.data["items"][0]["abc_class"]=="A"

def test_slotting():
    r=slotting.execute({"items":[{"sku":"fast","picks_per_day":40,"cube_m3":1}]})
    assert r.ok and r.data["recommendations"][0]["recommended_zone"]=="forward-pick"

def test_replenishment():
    r=replenish.execute({"average_daily_demand":10,"lead_time_days":5,"demand_stddev_daily":2,"service_level":0.95})
    assert r.ok and r.data["reorder_point"]>50

def test_capacity():
    r=capacity.execute({"used_volume_m3":85,"total_volume_m3":100,"usable_ratio":0.8})
    assert r.ok and r.data["status"]=="over-capacity"
