#memory grid game

import random
import time
import os

grid_size = 5
total_cells =grid_size * grid_size

sequence = []
score = 0

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def show_grid(highlight=None):
    for i in range(1, total_cells+1):
        if highlight == i:
            print(f"[{i:02}]", end="")
        else:
            print(f"{i:02}", end="")

        if i % grid_size == 0:
            print()
    print()

def show_sequence():
    clear()
    print("Memorize the sequence")
    for cell in sequence:
        show_grid(cell)
        time.sleep(0.8)
        clear()
        time.sleep(0.3)

def get_input():
    try:
        inp = input("Enter the sequence (space separated):")
        return list(map(int, inp.split()))
    except:
        return []

def game():
    global score

    print("------MEMORY GRID GAME------")
    input("Press Enter to start...")

    while True:
        clear()
        new_cell = random.randint(1, total_cells)
        sequence.append(new_cell)

        show_sequence()

        print("ur turn")
        show_grid()
        player = get_input()

        if player != sequence:
            print("\n wrong sequence!")
            print("correct was:",sequence)
            print("ur score:",score)
            break
        
        score +=1
        print("correct")
        print("score:",score)
        time.sleep(1)

    print("game over")

game()