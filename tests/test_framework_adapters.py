from adapters.openai_adapter import OpenAIAdapter
from adapters.crewai_adapter import CrewAIAdapter
from adapters.claude_code_adapter import ClaudeCodeAdapter
from adapters.lyzr_adapter import LyzrAdapter
from core.agent_core import AgentCore


def payload():
    return {
        "used_volume_m3": 1,
        "total_volume_m3": 10,
        "usable_ratio": 0.8,
    }


def test_openai_adapter():
    result = OpenAIAdapter(AgentCore()).invoke("assess-capacity", payload())
    assert result.success


def test_crewai_adapter():
    result = CrewAIAdapter(AgentCore()).invoke("assess-capacity", payload())
    assert result.success


def test_claude_code_adapter():
    result = ClaudeCodeAdapter(AgentCore()).invoke("assess-capacity", payload())
    assert result.success


def test_lyzr_adapter():
    result = LyzrAdapter(AgentCore()).invoke("assess-capacity", payload())
    assert result.success
