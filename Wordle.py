"""
Wordle Clone 🟩🟨⬛️
------------------

A simple command-line version of Wordle built in Python.

How to Play:
- Guess the secret 5-letter word within 6 tries.
- After each guess:
    🟩 = correct letter and position
    🟨 = letter is in the word but wrong position
    ⬛️ = letter is not in the word
"""

import random

global word
global guesses

class Guess:
    def __init__(self, guess):
        self.guess = []
        self.evaluated = []
        for x in range (0, 5):
            self.guess.append(guess[x])

    def Evaluate(self, word):
        for x in range (0, 5):
            if self.guess[x] == word[x]:
                self.evaluated.append("🟩")
            elif (self.guess[x] in word):
                self.evaluated.append("🟨")
            else:
                self.evaluated.append("⬛️")

    def Print(self):
        guess_string = ""
        evaluated_string = ""
        for x in range (0, 5):
            guess_string = guess_string + self.guess[x].upper() + "  "
            evaluated_string = evaluated_string + self.evaluated[x] + " "
        print(guess_string)
        print(evaluated_string)
        print ("---------------")

def GameOver():
    if all(x == "🟩" for x in guesses[-1].evaluated):
        print("You got it!")
        return False
    if len(guesses) == 6:
        print(f"You lost! The word was {word}")
        return False
    return True


Play = True
words = ["apple", "baker", "candy", "dance", "eagle", "flame", "grape", "happy", "input", "jelly", "knife", "lemon", "magic", "novel", "ocean", "paint", "queen", "radio", "shine", "tiger", "urban", "vivid", "waste", "xenon", "young", "zebra", "angle", "brave", "charm", "dream", "early", "faith", "giant", "honor", "ideal", "joint", "karma", "light", "mango", "noble", "olive", "peace", "quiet", "river", "solar", "trust", "unity", "vocal", "wheel", "xylem", "yacht", "zesty", "alarm", "brink", "claim", "dwarf", "envoy", "fancy", "glide", "hotel", "ivory", "judge", "karma", "laden", "merge", "night", "opera", "plaza", "quirk", "rally", "spike", "torch", "union", "vigor", "whale", "xenon", "yield", "zonal", "award", "blaze", "climb", "drift", "exile", "flair", "grind", "haste", "infer", "jolly", "knack", "laser", "mirth", "nerve", "oasis", "pride", "quirk", "realm", "smile", "tribe", "upset", "valor", "woven", "xerox", "youth", "zesty"]
word = random.choice(words)
guesses = []
while Play == True:
    guess = input("Enter your guess: ")
    while len(guess) != 5:
        guess = input("Please enter a word with 5 letters:")
    guesses.append(Guess(guess))
    guesses[-1].Evaluate(word)
    for x in range (0, len(guesses)):
        guesses[x].Print()
    Play = GameOver()