"""Environment-backed runtime configuration."""
from __future__ import annotations
import os


def _int(name: str, minimum: int = 1) -> int:
    value = os.getenv(name)
    if value is None:
        raise RuntimeError(f"Missing required environment variable: {name}")
    try:
        parsed = int(value)
    except ValueError as exc:
        raise RuntimeError(f"Environment variable {name} must be an integer") from exc
    if parsed < minimum:
        raise RuntimeError(f"Environment variable {name} must be >= {minimum}")
    return parsed


def _float(name: str, minimum: float = 0.0, maximum: float | None = None) -> float:
    value = os.getenv(name)
    if value is None:
        raise RuntimeError(f"Missing required environment variable: {name}")
    try:
        parsed = float(value)
    except ValueError as exc:
        raise RuntimeError(f"Environment variable {name} must be numeric") from exc
    if parsed < minimum or (maximum is not None and parsed > maximum):
        raise RuntimeError(f"Environment variable {name} is outside the allowed range")
    return parsed


class Settings:
    def __init__(self) -> None:
        self.log_level = os.getenv("WAREHOUSE_AGENT_LOG_LEVEL")
        if not self.log_level:
            raise RuntimeError("Missing required environment variable: WAREHOUSE_AGENT_LOG_LEVEL")
        self.timeout_seconds = _int("WAREHOUSE_AGENT_TIMEOUT_SECONDS")
        self.max_input_records = _int("WAREHOUSE_AGENT_MAX_INPUT_RECORDS")
        self.default_service_level = _float("WAREHOUSE_AGENT_DEFAULT_SERVICE_LEVEL", 0.0, 1.0)
        self.default_lead_time_days = _int("WAREHOUSE_AGENT_DEFAULT_LEAD_TIME_DAYS")
        self.default_review_period_days = _int("WAREHOUSE_AGENT_DEFAULT_REVIEW_PERIOD_DAYS")
        self.max_forecast_horizon_days = _int("WAREHOUSE_AGENT_MAX_FORECAST_HORIZON_DAYS")
