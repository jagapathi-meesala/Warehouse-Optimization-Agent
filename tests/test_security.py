from tools.assess_capacity import TOOL

def test_missing_field_rejected():
    r=TOOL.execute({"used_volume_m3":1})
    assert not r.ok and "Missing required field" in r.error["message"]

def test_negative_capacity_rejected():
    r=TOOL.execute({"used_volume_m3":-1,"total_volume_m3":10,"usable_ratio":0.8})
    assert not r.ok

def test_wrong_type_rejected():
    r=TOOL.execute({"used_volume_m3":"1","total_volume_m3":10,"usable_ratio":0.8})
    assert not r.ok

def test_malformed_request_rejected():
    r=TOOL.execute([])
    assert not r.ok
