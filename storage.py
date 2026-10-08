
import os
import pandas as pd


COLUMNS = [
    "Game_ID",
    "Player",
    "Date",
    "Target",
    "Attempts",
    "Result",
    "Score"
]


def initialize_file(filename):
    """Create the CSV file if it does not exist."""

    if not os.path.exists(filename):
        pd.DataFrame(columns=COLUMNS).to_csv(
            filename,
            index=False
        )


def load_games(filename):
    """Load game history from CSV."""

    initialize_file(filename)

    try:
        df = pd.read_csv(filename)

        if not df.empty:
            df["Game_ID"] = pd.to_numeric(
                df["Game_ID"],
                errors="coerce"
            )

            df["Attempts"] = pd.to_numeric(
                df["Attempts"],
                errors="coerce"
            )

            df["Score"] = pd.to_numeric(
                df["Score"],
                errors="coerce"
            )

        return df

    except Exception as e:
        print("Error loading file:", e)

        return pd.DataFrame(columns=COLUMNS)


def save_game(filename, record):
    """Save one game record."""

    initialize_file(filename)

    new_record = pd.DataFrame([record])

    new_record.to_csv(
        filename,
        mode="a",
        header=False,
        index=False
    )


def get_next_game_id(filename):
    """Get the next Game ID."""

    df = load_games(filename)

    if df.empty:
        return 1

    return int(df["Game_ID"].max()) + 1


def update_game(filename, game_id, updates):
    """Update an existing game record."""

    df = load_games(filename)

    if game_id not in df["Game_ID"].values:
        return False

    for key, value in updates.items():

        if key in df.columns:
            df.loc[
                df["Game_ID"] == game_id,
                key
            ] = value

    df.to_csv(
        filename,
        index=False
    )

    return True


def delete_game(filename, game_id):
    """Delete a game record."""

    df = load_games(filename)

    if game_id not in df["Game_ID"].values:
        return False

    df = df[
        df["Game_ID"] != game_id
    ]

    df.to_csv(
        filename,
        index=False
    )

    return True


print("storage.py created successfully!")
