"""Claude Code-compatible adapter boundary."""

from adapters.framework_adapter import FrameworkAdapter


class ClaudeCodeAdapter(FrameworkAdapter):
    framework_name = "claude-code"
