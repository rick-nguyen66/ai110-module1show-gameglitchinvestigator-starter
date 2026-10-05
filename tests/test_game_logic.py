from pathlib import Path
from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result, _ = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result, _ = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result, _ = check_guess(40, 50)
    assert result == "Too Low"


def test_new_game_resets_state():
    # After a finished game, New Game should fully reset the session state
    from streamlit.testing.v1 import AppTest

    at = AppTest.from_file(str(Path(__file__).resolve().parent.parent / "app.py")).run()
    at.session_state["status"] = "lost"
    at.session_state["score"] = 42
    at.session_state["attempts"] = 8
    at.session_state["history"] = [1, 2, 3]

    next(b for b in at.button if "New Game" in b.label).click()
    at.run()

    assert at.session_state["status"] == "playing"
    assert at.session_state["score"] == 0
    assert at.session_state["attempts"] == 1
    assert at.session_state["history"] == []
    # Default difficulty is Normal (1-100)
    assert 1 <= at.session_state["secret"] <= 100
    assert not at.exception
