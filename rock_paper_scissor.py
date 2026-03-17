import random

options = ("rock", "paper", "scissor")

running = True

while running:
    player = None
    computer = random.choice(options)
    while player not in options:
        player = input("Enter ur choice(rock, paper, scissor): ")
        
    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie")
    elif player == "rock" and computer == "scissor":
        print("U win!")
    elif player == "paper" and computer == "rock":
        print("U win!")
    elif player == "scissor" and computer == "paper":
        print("u win!")
    else:
        print("U lose")

    if not input("play again? (y/n: )").lower() == "y":
        running = False

print("thanks for playing!")