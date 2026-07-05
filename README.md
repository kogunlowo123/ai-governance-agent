# AI Governance Agent

[![CI](https://github.com/kogunlowo123/ai-governance-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/ai-governance-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: AI Engineering | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

AI governance and compliance agent that manages model registries, tracks model lineage, enforces responsible AI policies, conducts bias audits, and generates compliance documentation for regulatory frameworks.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `register_model` | Register a model with metadata, lineage, and governance tags |
| `audit_bias` | Run bias audit across demographic groups for a model |
| `check_compliance` | Check model compliance against regulatory frameworks |
| `generate_model_card` | Generate a model card with intended use, limitations, and performance |
| `enforce_policy` | Enforce governance policy on model deployment decisions |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/governance/register` | Register model |
| `POST` | `/api/v1/governance/audit-bias` | Audit bias |
| `POST` | `/api/v1/governance/compliance` | Check compliance |
| `POST` | `/api/v1/governance/model-card` | Generate model card |
| `POST` | `/api/v1/governance/enforce-policy` | Enforce policy |

## Features

- Model Registry
- Lineage Tracking
- Policy Enforcement
- Bias Auditing
- Compliance Reporting

## Integrations

- Mlflow
- Weights Biases
- Sagemaker Registry
- Vertex Model Registry
- Aequitas

## Architecture

```
ai-governance-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── ai_governance_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**MLflow + Model Registry + Compliance Frameworks**

---

Built as part of the Enterprise AI Agent Platform.
