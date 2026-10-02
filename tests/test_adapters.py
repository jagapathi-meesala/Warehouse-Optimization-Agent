def test_portable_adapter():
    from adapters.portable_adapter import RegistryAdapter
    from core.agent_core import AgentCore
    adapter=RegistryAdapter(AgentCore())
    result=adapter.invoke("assess-capacity", {"used_volume_m3":1,"total_volume_m3":10,"usable_ratio":0.8})
    assert result.success and result.payload["utilization"]==0.125
