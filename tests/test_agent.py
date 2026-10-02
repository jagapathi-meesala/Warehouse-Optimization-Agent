import os

def _env(monkeypatch):
    for k,v in {"WAREHOUSE_AGENT_LOG_LEVEL":"INFO","WAREHOUSE_AGENT_TIMEOUT_SECONDS":"30","WAREHOUSE_AGENT_MAX_INPUT_RECORDS":"10000","WAREHOUSE_AGENT_DEFAULT_SERVICE_LEVEL":"0.95","WAREHOUSE_AGENT_DEFAULT_LEAD_TIME_DAYS":"7","WAREHOUSE_AGENT_DEFAULT_REVIEW_PERIOD_DAYS":"7","WAREHOUSE_AGENT_MAX_FORECAST_HORIZON_DAYS":"365"}.items(): monkeypatch.setenv(k,v)

def test_agent_discovers_tools(monkeypatch):
    _env(monkeypatch)
    from core.agent_core import AgentCore
    agent=AgentCore()
    assert agent.registry.names()==["analyze-inventory","assess-capacity","calculate-replenishment","recommend-slotting"]

def test_unknown_tool_is_structured_error(monkeypatch):
    _env(monkeypatch)
    from core.agent_core import AgentCore
    r=AgentCore().execute("missing", {})
    assert not r.ok and r.error["type"]=="UnknownTool"
