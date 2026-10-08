
import pandas as pd
import numpy as np


def calculate_statistics(df):
    """Calculate overall game statistics."""

    if df.empty:
        return {}

    total_games = len(df)

    successful_games = len(
        df[df["Result"].str.lower() == "success"]
    )

    failed_games = total_games - successful_games

    success_rate = (
        successful_games / total_games
    ) * 100

    average_attempts = df["Attempts"].mean()

    minimum_attempts = df["Attempts"].min()

    maximum_attempts = df["Attempts"].max()

    successful_df = df[
        df["Result"].str.lower() == "success"
    ]

    if not successful_df.empty:

        average_successful_attempts = (
            successful_df["Attempts"].mean()
        )

    else:

        average_successful_attempts = 0

    return {
        "Total Games": total_games,
        "Successful Games": successful_games,
        "Failed Games": failed_games,
        "Success Rate": round(success_rate, 2),
        "Average Attempts": round(
            average_attempts, 2
        ),
        "Minimum Attempts": int(
            minimum_attempts
        ),
        "Maximum Attempts": int(
            maximum_attempts
        ),
        "Average Successful Attempts": round(
            average_successful_attempts, 2
        )
    }


def search_by_player(df, player):
    """Search games played by a player."""

    return df[
        df["Player"].str.lower() ==
        player.lower()
    ]


def filter_by_result(df, result):
    """Filter games by result."""

    return df[
        df["Result"].str.lower() ==
        result.lower()
    ]


def filter_by_date(
    df,
    start_date,
    end_date
):
    """Filter games between two dates."""

    temp = df.copy()

    temp["Date"] = pd.to_datetime(
        temp["Date"]
    )

    start = pd.to_datetime(start_date)

    end = pd.to_datetime(end_date)

    return temp[
        (temp["Date"] >= start) &
        (temp["Date"] <= end)
    ]


def player_comparison(df):
    """Compare player performance."""

    if df.empty:
        return pd.DataFrame()

    comparison = df.groupby(
        "Player"
    ).agg(
        Games=("Game_ID", "count"),

        Average_Attempts=(
            "Attempts",
            "mean"
        ),

        Success_Rate=(
            "Result",
            lambda x:
            (x.str.lower() == "success").mean()
            * 100
        )
    ).reset_index()

    comparison["Average_Attempts"] = (
        comparison["Average_Attempts"]
        .round(2)
    )

    comparison["Success_Rate"] = (
        comparison["Success_Rate"]
        .round(2)
    )

    return comparison


def monthly_analysis(df):
    """Calculate monthly attempt statistics."""

    temp = df.copy()

    temp["Date"] = pd.to_datetime(
        temp["Date"]
    )

    temp["Month"] = (
        temp["Date"]
        .dt.to_period("M")
        .astype(str)
    )

    result = temp.groupby(
        "Month"
    ).agg(
        Average_Attempts=(
            "Attempts",
            "mean"
        ),

        Games=(
            "Game_ID",
            "count"
        )
    ).reset_index()

    result["Average_Attempts"] = (
        result["Average_Attempts"]
        .round(2)
    )

    return result


print("analytics.py created successfully!")
