"""CrewAI-compatible adapter boundary."""

from adapters.framework_adapter import FrameworkAdapter


class CrewAIAdapter(FrameworkAdapter):
    framework_name = "crewai"
