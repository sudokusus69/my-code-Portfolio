import random

def stone_paper_scissors():
    msg = input("Enter your choice (rock, paper, scissors): ").lower()
    comp = random.choice(["rock", "paper", "scissors"])

    if msg == comp:
        print(f"Both chose {msg}. It's a tie!")
    elif (msg == "rock" and comp == "scissors") or \
         (msg == "paper" and comp == "rock") or \
         (msg == "scissors" and comp == "paper"):
        print(f"You chose {msg} and the computer chose {comp}. You win!")
    elif (msg == "rock" and comp == "paper") or \
         (msg == "paper" and comp == "scissors") or \
         (msg == "scissors" and comp == "rock"):
        print(f"You chose {msg} and the computer chose {comp}. You lose!")
    else:
        print("Invalid input. Please enter rock, paper, or scissors.")



stone_paper_scissors()