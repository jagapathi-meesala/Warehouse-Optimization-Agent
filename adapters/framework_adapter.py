"""Framework adapter base for the Warehouse Optimization Agent."""
from __future__ import annotations

from typing import Any

from adapters.portable_adapter import AdapterResponse, PortableAdapter


class FrameworkAdapter(PortableAdapter):
    """Base adapter that translates framework calls to AgentCore."""

    framework_name = "framework-independent"

    def __init__(self, agent_core: Any) -> None:
        self.agent_core = agent_core

    def invoke(self, tool_name: str, arguments: dict[str, Any]) -> AdapterResponse:
        result = self.agent_core.execute(tool_name, arguments)
        return AdapterResponse(
            success=result.ok,
            payload=result.data if result.ok else result.error or {},
        )
