
from typing import Literal

from pydantic import BaseModel, Field


class EmailAnalysis(BaseModel):
    """Structured analysis of an email."""

    intent: Literal[
        "question",
        "complaint",
        "job_application",
        "meeting_request",
        "other",
    ]

    priority: Literal["low", "normal", "high"]

    summary: str = Field(min_length=1)

    suggested_reply: str = Field(min_length=1)

    key_points: list[str]
