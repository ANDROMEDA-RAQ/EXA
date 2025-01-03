import tkinter as tk


class LeaderboardApp:
    def __init__(self, master):
        self.master = master
        master.title("Leaderboard")
        master.geometry("300x400")  # Adjust size as needed

        # Create the main frame
        self.main_frame = tk.Frame(master, bg="white")
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Title
        self.title_label = tk.Label(
            self.main_frame, text="Leaderboard", font=("Arial", 18, "bold"), bg="white"
        )
        self.title_label.pack(pady=(0, 10))

        # Create a list of leaderboard entries
        self.leaderboard_entries = [
            ("Player 1", 100),
            ("Player 2", 90),
            ("Player 3", 85),
            ("Player 4", 80),
            ("Player 5", 75),
        ]

        # Create a frame for the leaderboard
        self.list_frame = tk.Frame(self.main_frame, bg="white")
        self.list_frame.pack(fill=tk.BOTH, expand=True)

        for rank, (player, score) in enumerate(self.leaderboard_entries, 1):
            # Create labels for each entry
            rank_label = tk.Label(
                self.list_frame,
                text=f"{rank}.",
                font=("Arial", 12),
                bg="white",
                anchor="w",
            )
            player_label = tk.Label(
                self.list_frame, text=player, font=("Arial", 12), bg="white", anchor="w"
            )
            score_label = tk.Label(
                self.list_frame,
                text=str(score),
                font=("Arial", 12),
                bg="white",
                anchor="e",
            )

            # Arrange labels in a grid
            rank_label.grid(row=rank - 1, column=0, sticky="w", padx=(0, 10))
            player_label.grid(row=rank - 1, column=1, sticky="w")
            score_label.grid(row=rank - 1, column=2, sticky="e")

        # Adjust for better visual alignment
        self.list_frame.columnconfigure(1, weight=1)


if __name__ == "__main__":
    root = tk.Tk()
    app = LeaderboardApp(root)
    root.mainloop()
