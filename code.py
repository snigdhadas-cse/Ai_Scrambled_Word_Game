import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import random, json, time, threading
import requests

# -------------------------------
# Utility Functions
# -------------------------------

def fetch_meaning(word):
    """Try to fetch definition from dictionary API."""
    try:
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        r = requests.get(url, timeout=3)
        data = r.json()
        meaning = data[0]["meanings"][0]["definitions"][0]["definition"]
        return meaning
    except:
        return "No definition available."

def scramble_word(word):
    letters = list(word)
    random.shuffle(letters)
    return "".join(letters)

# -------------------------------
# Main Game Class
# -------------------------------

class ScrambleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🎉 Scrambled Word Game")
        self.root.geometry("700x540")
        self.root.configure(bg="#FFB6C1")

        self.transition_colors = ["#FFB6C1", "#FFC9DE", "#FFDDF0", "#FFEAF9"]
        self.color_index = 0
        self.animate_background()

        # Game variables
        self.score = 0
        self.time_left = 60
        self.current_word = ""
        self.scrambled = ""
        self.hints_used = 0
        self.mode = "Normal"
        self.game_running = False

        # Word list
        self.words = ["python", "program", "challenge", "scramble", "rainbow",
                      "creative", "project", "developer", "internet", "colorful"]

        self.create_ui()

    # -------------------------------
    # Animated Background
    # -------------------------------
    def animate_background(self):
        self.root.configure(bg=self.transition_colors[self.color_index])
        self.color_index = (self.color_index + 1) % len(self.transition_colors)
        self.root.after(1500, self.animate_background)

    # -------------------------------
    # UI Creation
    # -------------------------------
    def create_ui(self):
        title = tk.Label(
            self.root,
            text="✨ Scrambled Word Game ✨",
            font=("Comic Sans MS", 26, "bold"),
            bg=self.root["bg"],
            fg="#4B0082"
        )
        title.pack(pady=10)

        # Word Display
        self.word_label = tk.Label(
            self.root,
            text="Click Start!",
            font=("Arial", 28, "bold"),
            bg=self.root["bg"],
            fg="#8A2BE2"
        )
        self.word_label.pack(pady=25)

        # Entry
        self.entry = tk.Entry(
            self.root,
            font=("Arial", 18),
            justify="center",
            bd=5,
            relief="groove"
        )
        self.entry.pack(pady=10)

        # Buttons Frame
        btn_frame = tk.Frame(self.root, bg=self.root["bg"])
        btn_frame.pack(pady=10)

        tk.Button(
            btn_frame,
            text="Submit",
            font=("Arial", 14, "bold"),
            bg="#77DD77",
            width=10,
            command=self.check_answer
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            btn_frame,
            text="Hint",
            font=("Arial", 14, "bold"),
            bg="#FFEA00",
            width=10,
            command=self.show_hint
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            btn_frame,
            text="New Word",
            font=("Arial", 14, "bold"),
            bg="#ADD8E6",
            width=10,
            command=self.new_word
        ).grid(row=0, column=2, padx=5)

        # Score + Timer
        info_frame = tk.Frame(self.root, bg=self.root["bg"])
        info_frame.pack(pady=10)

        self.score_label = tk.Label(
            info_frame, text="Score: 0", font=("Arial", 16, "bold"),
            bg=self.root["bg"], fg="#4B0082"
        )
        self.score_label.grid(row=0, column=0, padx=20)

        self.timer_label = tk.Label(
            info_frame, text="Time Left: 60", font=("Arial", 16, "bold"),
            bg=self.root["bg"], fg="#4B0082"
        )
        self.timer_label.grid(row=0, column=1, padx=20)

        # Word Meaning
        self.meaning_label = tk.Label(
            self.root,
            text="Word meaning will appear here.",
            font=("Arial", 14),
            wraplength=600,
            bg=self.root["bg"],
            fg="#333333"
        )
        self.meaning_label.pack(pady=15)

        # Bottom Buttons
        bottom = tk.Frame(self.root, bg=self.root["bg"])
        bottom.pack(pady=10)

        tk.Button(
            bottom,
            text="Start Game",
            font=("Arial", 14, "bold"),
            bg="#FF7F50",
            width=12,
            command=self.start_game
        ).grid(row=0, column=0, padx=8)

        tk.Button(
            bottom,
            text="Save Game",
            font=("Arial", 14, "bold"),
            bg="#AFEEEE",
            width=12,
            command=self.save_game
        ).grid(row=0, column=1, padx=8)

        tk.Button(
            bottom,
            text="Load Game",
            font=("Arial", 14, "bold"),
            bg="#F4A460",
            width=12,
            command=self.load_game
        ).grid(row=0, column=2, padx=8)

    # -------------------------------
    # Game Logic
    # -------------------------------
    def start_game(self):
        self.score = 0
        self.time_left = 60
        self.game_running = True
        self.update_ui()
        self.new_word()
        threading.Thread(target=self.timer_thread, daemon=True).start()

    def update_ui(self):
        self.score_label.config(text=f"Score: {self.score}")
        self.timer_label.config(text=f"Time Left: {self.time_left}")

    def timer_thread(self):
        while self.time_left > 0 and self.game_running:
            time.sleep(1)
            self.time_left -= 1
            self.timer_label.config(text=f"Time Left: {self.time_left}")
        if self.time_left <= 0:
            self.end_game()

    def end_game(self):
        self.game_running = False
        messagebox.showinfo("Game Over!", f"Your final score: {self.score}")

    def new_word(self):
        self.current_word = random.choice(self.words)
        self.scrambled = scramble_word(self.current_word)

        self.word_label.config(text=self.scrambled)
        self.entry.delete(0, tk.END)

        meaning = fetch_meaning(self.current_word)
        self.meaning_label.config(text=f"Hint/Meaning: {meaning}")

    def check_answer(self):
        if self.entry.get().lower() == self.current_word.lower():
            self.score += 10
            self.update_ui()
            self.new_word()
        else:
            messagebox.showwarning("Wrong!", "Incorrect guess!")

    def show_hint(self):
        hint = f"Starts with: {self.current_word[0]}"
        messagebox.showinfo("Hint", hint)

    # -------------------------------
    # Save + Load System
    # -------------------------------
    def save_game(self):
        data = {
            "score": self.score,
            "time_left": self.time_left,
            "current_word": self.current_word,
            "scrambled": self.scrambled
        }
        with open("save.json", "w") as f:
            json.dump(data, f)
        messagebox.showinfo("Saved", "Game progress saved!")

    def load_game(self):
        try:
            with open("save.json", "r") as f:
                data = json.load(f)

            self.score = data["score"]
            self.time_left = data["time_left"]
            self.current_word = data["current_word"]
            self.scrambled = data["scrambled"]

            self.word_label.config(text=self.scrambled)
            self.update_ui()
            messagebox.showinfo("Loaded", "Game loaded successfully!")
        except:
            messagebox.showerror("Error", "No save file found!")

# -------------------------------
# Run App
# -------------------------------
root = tk.Tk()
app = ScrambleGame(root)
root.mainloop()
