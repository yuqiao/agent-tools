"""Models for agent tools."""

from pydantic import BaseModel


class AgentTool(BaseModel):
    """Base model for agent tools."""
    name: str
    description: str
    parameters: dict