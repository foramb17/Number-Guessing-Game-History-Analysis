
import pandas as pd
import matplotlib.pyplot as plt


def attempt_distribution(df):
    """Create a histogram of attempts per game."""

    plt.figure(figsize=(8, 5))

    plt.hist(
        df["Attempts"],
        bins=range(
            int(df["Attempts"].min()),
            int(df["Attempts"].max()) + 2
        ),
        edgecolor="black"
    )

    plt.title(
        "Distribution of Attempts per Game"
    )

    plt.xlabel("Number of Attempts")
    plt.ylabel("Number of Games")

    plt.grid(
        axis="y",
        alpha=0.3
    )

    plt.show()


def monthly_attempts(df):
    """Create a line chart of monthly attempts."""

    temp = df.copy()

    temp["Date"] = pd.to_datetime(
        temp["Date"]
    )

    temp["Month"] = (
        temp["Date"]
        .dt.to_period("M")
        .astype(str)
    )

    monthly = temp.groupby(
        "Month"
    )["Attempts"].mean()

    plt.figure(figsize=(9, 5))

    plt.plot(
        monthly.index,
        monthly.values,
        marker="o",
        linewidth=2
    )

    plt.title(
        "Average Attempts by Month"
    )

    plt.xlabel("Month")
    plt.ylabel("Average Attempts")

    plt.grid(
        True,
        alpha=0.3
    )

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.show()


print("reports.py created successfully!")
