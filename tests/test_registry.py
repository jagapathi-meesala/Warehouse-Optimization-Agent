def test_registry_dynamic_discovery():
    from core.agent_core import ToolRegistry
    r=ToolRegistry(); r.discover(); assert len(r.names())==4

def test_duplicate_registration_rejected():
    from core.agent_core import ToolRegistry
    from tools.assess_capacity import TOOL
    r=ToolRegistry(); r.register(TOOL)
    try: r.register(TOOL)
    except ValueError: pass
    else: raise AssertionError("duplicate registration should fail")
