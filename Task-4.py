#Stone, Paper, Scissors GAME

import tkinter as tk
from tkinter import messagebox
import random

# Game logic
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

#play a round
def play_round(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(["rock", "paper", "scissors"])
    
    result = determine_winner(user_choice, computer_choice)
    
    if result == "user":
        user_score += 1
        result_text = "You win!"
    elif result == "computer":
        computer_score += 1
        result_text = "Computer wins!"
    else:
        result_text = "It's a tie!"
    
    result_label.config(text=f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n{result_text}")
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")
    
# reset the game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="")
    score_label.config(text="Score - You: 0 | Computer: 0")

# main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# Initialize scores
user_score = 0
computer_score = 0

#buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Label(button_frame, text="Choose your move:").pack()

tk.Button(button_frame, text="Rock", command=lambda: play_round("rock")).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Paper", command=lambda: play_round("paper")).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Scissors", command=lambda: play_round("scissors")).pack(side=tk.LEFT, padx=5)

#display results
result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack(pady=10)

#display score
score_label = tk.Label(root, text="Score - You: 0 | Computer: 0", font=("Helvetica", 12))
score_label.pack(pady=10)

#reset the game
reset_button = tk.Button(root, text="Reset Game", command=reset_game)
reset_button.pack(pady=10)

#event loop
root.mainloop()
