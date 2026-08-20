Wordle.py
A command line word guessing game written in Python.

Quick Start
Open your terminal and run the script:

python Wordle.py

Game Rules
You have 6 attempts to guess a hidden 5 letter word.
Every guess must be exactly 5 letters long.
Feedback is displayed using colored blocks after every round:
🟩 Correct letter in the correct spot
🟨 Correct letter in the wrong spot
⬛️ Letter is not in the word
Code Structure
Guess Class: Handles parsing individual guesses, checking letter positions, and formatting console output.
Game Loop: Manages random word selection from an internal dictionary, validates input length, and evaluates win or loss conditions via GameOver()
