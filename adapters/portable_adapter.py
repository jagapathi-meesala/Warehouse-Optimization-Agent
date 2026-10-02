"""Portable adapter protocol and framework-neutral request/response mapping."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Protocol


@dataclass(frozen=True)
class AdapterResponse:
    success: bool
    payload: dict[str, Any]


class PortableAdapter(Protocol):
    framework_name: str

    def invoke(self, tool_name: str, arguments: dict[str, Any]) -> AdapterResponse: ...


class RegistryAdapter:
    """Adapter implementation that depends only on the local AgentCore."""
    framework_name = "framework-independent"

    def __init__(self, agent_core: Any) -> None:
        self.agent_core = agent_core

    def invoke(self, tool_name: str, arguments: dict[str, Any]) -> AdapterResponse:
        result = self.agent_core.execute(tool_name, arguments)
        return AdapterResponse(success=result.ok, payload=result.data if result.ok else result.error or {})
