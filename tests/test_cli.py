from email_assistant.cli import main
from unittest.mock import patch
from email_assistant.models import EmailAnalysis

@patch("email_assistant.cli.analyze_email")
@patch("builtins.input")
def test_main(mock_input,mock_analyze, capsys):
    mock_input.return_value="Could we reschedule our meeting?"

    mock_analyze.return_value=EmailAnalysis(
                intent="question",
                priority="normal",
                summary="The sender asks about a meeting.",
                suggested_reply="Hello, the meeting is scheduled for Monday.",
                key_points=["Meeting", "Monday"]
            )
    main()
    captured = capsys.readouterr()
    output = captured.out

    assert "priority : normal" in output
    assert "summary : The sender asks about a meeting." in output
    assert "suggested reply : Hello, the meeting is scheduled for Monday."  in output 
    assert "key points :\n-Meeting\n-Monday" in output
    mock_input.assert_called_once_with("Enter your email:")
    mock_analyze.assert_called_once_with("Could we reschedule our meeting?")