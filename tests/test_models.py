
import pytest
from pydantic import ValidationError

from email_assistant.models import EmailAnalysis


def test_valid_email_analysis():
    analysis = EmailAnalysis(
        intent="question",
        priority="normal",
        summary="The sender asks about a meeting.",
        suggested_reply="Hello, the meeting is scheduled for Monday.",
        key_points=["Meeting", "Monday"],
    )

    assert analysis.intent == "question"
    assert analysis.priority == "normal"
    assert len(analysis.key_points) == 2