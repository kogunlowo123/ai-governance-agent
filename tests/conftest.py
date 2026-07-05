"""Test configuration for AI Governance Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "ai-governance-agent", "category": "AI Engineering"}
