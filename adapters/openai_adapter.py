"""OpenAI-compatible adapter boundary.

This module intentionally does not import the OpenAI SDK. It exposes the
portable tool invocation contract so an OpenAI runtime can bind it without
making the core agent dependent on that SDK.
"""
from adapters.framework_adapter import FrameworkAdapter


class OpenAIAdapter(FrameworkAdapter):
    framework_name = "openai"
