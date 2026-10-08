
import tkinter as tk
from tkinter import messagebox


def create_gui():

    root = tk.Tk()

    root.title(
        "Number Guessing Game - "
        "Performance Analyzer"
    )

    root.geometry("500x450")

    title = tk.Label(
        root,
        text="NUMBER GUESSING GAME",
        font=("Arial", 18, "bold")
    )

    title.pack(pady=20)

    subtitle = tk.Label(
        root,
        text="History & Statistical Analysis",
        font=("Arial", 12)
    )

    subtitle.pack(pady=5)

    buttons = [
        "Play New Game",
        "View History",
        "Search / Filter",
        "Statistics",
        "Compare Players",
        "Reports",
        "Exit"
    ]

    for button_name in buttons:

        if button_name == "Exit":

            command = root.destroy

        else:

            command = lambda name=button_name: (
                messagebox.showinfo(
                    "Project Feature",
                    name + " selected"
                )
            )

        tk.Button(
            root,
            text=button_name,
            width=25,
            command=command
        ).pack(pady=5)

    root.mainloop()
