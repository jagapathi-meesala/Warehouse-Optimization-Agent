"""Dynamic tool registry and execution core."""
from __future__ import annotations
from importlib import import_module
from pathlib import Path
from typing import Any
from contracts.tool_contract import ToolContract, ToolResult


class ToolRegistry:
    def __init__(self) -> None:
        self._tools: dict[str, ToolContract] = {}

    def register(self, tool: ToolContract) -> None:
        name = tool.metadata.name
        if name in self._tools:
            raise ValueError(f"Tool already registered: {name}")
        self._tools[name] = tool

    def discover(self, package: str = "tools") -> None:
        package_path = Path(__file__).resolve().parents[1] / package
        for path in sorted(package_path.glob("*.py")):
            if path.name.startswith("_"):
                continue
            module = import_module(f"{package}.{path.stem}")
            tool = getattr(module, "TOOL", None)
            if isinstance(tool, ToolContract):
                self.register(tool)

    def names(self) -> list[str]:
        return sorted(self._tools)

    def get(self, name: str) -> ToolContract:
        try:
            return self._tools[name]
        except KeyError as exc:
            raise KeyError(f"Unknown tool: {name}") from exc

    def execute(self, name: str, payload: Any) -> ToolResult:
        try:
            return self.get(name).execute(payload)
        except KeyError as exc:
            return ToolResult(ok=False, error={"type": "UnknownTool", "message": str(exc)})


class AgentCore:
    def __init__(self) -> None:
        self.registry = ToolRegistry()
        self.registry.discover()

    def execute(self, tool_name: str, payload: Any) -> ToolResult:
        return self.registry.execute(tool_name, payload)
