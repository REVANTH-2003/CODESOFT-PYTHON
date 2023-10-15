import tkinter as tk
import random

# Global variables for score
user_score = 0
computer_score = 0

# Function to play a round of rock-paper-scissors
def play_round(user_choice):
    global user_score, computer_score

    # Map the computer's random choice to "rock," "paper," or "scissors"
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    # Determine the winner
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        result = "You win!"
        user_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1

    # Update the labels
    user_label.config(text=f"Your Choice: {user_choice}")
    computer_label.config(text=f"Computer's Choice: {computer_choice}")
    result_label.config(text=result)
    score_label.config(text=f"Your Score: {user_score} | Computer Score: {computer_score}")

# Function to start a new round
def new_round():
    user_label.config(text="Your Choice: ")
    computer_label.config(text="Computer's Choice: ")
    result_label.config(text="")
    play_round_button.config(state=tk.NORMAL)

# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# Create and place widgets
user_label = tk.Label(root, text="Your Choice: ")
user_label.pack()

choices_frame = tk.Frame(root)
choices_frame.pack()

rock_button = tk.Button(choices_frame, text="Rock", command=lambda: play_round("rock"))
paper_button = tk.Button(choices_frame, text="Paper", command=lambda: play_round("paper"))
scissors_button = tk.Button(choices_frame, text="Scissors", command=lambda: play_round("scissors"))

rock_button.pack(side=tk.LEFT)
paper_button.pack(side=tk.LEFT)
scissors_button.pack(side=tk.LEFT)

computer_label = tk.Label(root, text="Computer's Choice: ")
computer_label.pack()

result_label = tk.Label(root, text="")
result_label.pack()

score_label = tk.Label(root, text=f"Your Score: {user_score} | Computer Score: {computer_score}")
score_label.pack()

play_round_button = tk.Button(root, text="Play Round", command=new_round)
play_round_button.pack()

root.mainloop()
