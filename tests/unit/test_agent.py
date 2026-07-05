"""AI Governance Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_register_model():
    """Test Register a model with metadata, lineage, and governance tags."""
    tools = AgentTools()
    result = await tools.register_model(model_name="test", version="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_audit_bias():
    """Test Run bias audit across demographic groups for a model."""
    tools = AgentTools()
    result = await tools.audit_bias(model_id="test", test_data="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_check_compliance():
    """Test Check model compliance against regulatory frameworks."""
    tools = AgentTools()
    result = await tools.check_compliance(model_id="test", frameworks="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_generate_model_card():
    """Test Generate a model card with intended use, limitations, and performance."""
    tools = AgentTools()
    result = await tools.generate_model_card(model_id="test", include_eval_results=True)
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.ai_governance_agent_agent import AiGovernanceAgentAgent
    agent = AiGovernanceAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
