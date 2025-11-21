
# 🎉 Scrambled Word Game – Colourful Tkinter Edition

A fun, interactive, and visually engaging **Scrambled Word Game** built entirely using **Python + Tkinter (no pygame!)**.
This project features smooth UI transitions, playful colours, word meanings, hints, scoring, a countdown timer, and even a save/load system to continue gameplay later.

Perfect for Python beginners, students, and anyone looking to create a beautiful and functional desktop game.

---

## ✨ Features

### 🎨 **Playful & Colourful UI**

* Soft animated background colour transitions
* Modern, clean, attractive, playful theme
* Big, readable fonts (Comic Sans / Arial)
* Buttons and labels styled for a game-like experience

### 🎮 **Core Gameplay**

* Scrambled word shown on screen
* Type your guess in the input box
* +10 score for every correct guess
* “New Word” button to skip to another word
* “Submit” button to check your answer

### 🧩 **Game Modes & Logic**

* 60–second timer (auto countdown)
* Game ends when timer reaches 0
* Hint feature (First letter reveal)
* Fetches real word meanings from Dictionary API
* Offline fallback if no internet

### 💾 **Save & Load Game**

* Saves:

  * Score
  * Time left
  * Current real word
  * Current scrambled word
* Load your game anytime using a simple JSON system

### 📘 **Word Meaning / Hint System**

Each new word automatically shows:

* Word meaning (from API)
* Hint button (first letter reveal)

### 📂 **Custom Word List**

Built-in word list includes 10+ words.
Easily extend by editing Python list or hooking custom file loader.

---

## 🛠 Tech Stack

* **Python 3.x**
* **Tkinter** – GUI
* **JSON** – Save/Load system
* **Requests** – Dictionary API

No additional dependencies. **Fully standalone.**

---

## 📸 Screenshots

*(Optional: You can add screenshots here if you have them)*

```
/screenshots
    - game_home.png
    - game_play.png
    - save_load.png
```

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/snigdhadas-cse/Ai_Scrambled_Word_Game.git
cd Ai_Scrambled_Word_Game
```

### 2. Install required package

Only `requests` is needed:

```bash
pip install requests
```

### 3. Run the Game

```bash
python code.py
```

That’s it! 🎮
No pygame, no heavy dependencies.

---

## 🧠 How the Game Works

1. Game picks a random word
2. Letters are shuffled
3. Meaning is fetched from API
4. Timer starts
5. Player guesses word
6. Score increases
7. Game auto-ends when timer reaches 0

---

## 📦 Save / Load System

When the user clicks **Save Game**, a `save.json` file is created with:

```json
{
  "score": 40,
  "time_left": 23,
  "current_word": "python",
  "scrambled": "htpyno"
}
```

When **Load Game** is clicked:

* The game state is restored
* Scrambled word & meaning shown again

---

## 🧩 Future Enhancements

*(Optional but good for GitHub)*

* 🔊 Add sound effects
* 🎵 Add background music
* 🌈 Add gradients & theme selector
* 🧠 Add difficulty levels
* 🔤 Add long/short words mode
* 🌐 Add leaderboard using Firebase or MongoDB

---

## 🤝 Contributing

Contributions are welcome!
Feel free to:

* Fork the repo
* Add features
* Submit issues
* Create pull requests

Let’s build something awesome together 🚀

---

## 📜 License

This project is licensed under the **MIT License**.
You are free to use, modify, and distribute it.
