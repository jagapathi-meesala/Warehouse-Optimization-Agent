"""Framework-independent tool contract."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Callable, Mapping


@dataclass(frozen=True)
class ToolMetadata:
    name: str
    description: str
    input_schema: Mapping[str, Any]


@dataclass(frozen=True)
class ToolResult:
    ok: bool
    data: dict[str, Any] | None = None
    error: dict[str, Any] | None = None


@dataclass(frozen=True)
class ToolContract:
    """Small interface shared by all domain tools."""
    metadata: ToolMetadata
    executor: Callable[[dict[str, Any]], dict[str, Any]]

    def validate(self, payload: Any) -> dict[str, Any]:
        if not isinstance(payload, dict):
            raise ValueError("Input must be a JSON object")
        required = self.metadata.input_schema.get("required", [])
        for key in required:
            if key not in payload:
                raise ValueError(f"Missing required field: {key}")
        return payload

    def execute(self, payload: Any) -> ToolResult:
        try:
            valid = self.validate(payload)
            return ToolResult(ok=True, data=self.executor(valid))
        except (ValueError, TypeError, ZeroDivisionError) as exc:
            return ToolResult(ok=False, error={"type": type(exc).__name__, "message": str(exc)})
        except Exception as exc:
            return ToolResult(ok=False, error={"type": "ToolExecutionError", "message": str(exc)})
