
import random
from datetime import datetime


def generate_target(low=1, high=100):
    """Generate a random target number."""
    return random.randint(low, high)


def check_guess(guess, target):
    """Check whether the guess is correct, too low, or too high."""

    if guess == target:
        return "Correct"

    elif guess < target:
        return "Too Low"

    else:
        return "Too High"


def calculate_score(attempts, success):
    """Calculate the player's score."""

    if not success:
        return 0

    score = max(100 - (attempts - 1) * 10, 10)

    return score


def create_game_record(
    game_id,
    player,
    target,
    attempts,
    result,
    score
):
    """Create one game record."""

    return {
        "Game_ID": game_id,
        "Player": player,
        "Date": datetime.now().strftime("%Y-%m-%d"),
        "Target": target,
        "Attempts": attempts,
        "Result": result,
        "Score": score
    }


print("game_engine.py created successfully!")
