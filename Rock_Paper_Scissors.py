import random

"""Rock paper Scissors game."""

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
x_points = 0
M_points = 0
i = 1

Moves = [rock, paper, scissors]

while i <= 3:
    Move = int(input("Choose 1 for Rock, 2 for Paper, or 3 for Scissors.\n"))
    x = random.randint(1, 3)
    if Move > 3:
        print("You've chosen a character other than what's been suggested")
    else:
        print(f"You chose {Moves[Move - 1]}\n The computer chose {Moves[x - 1]}")
        if (x == 1 and Move == 3) or (x == 2 and Move == 1) or (x == 3 and Move == 2):
            print("You lose")
            x_points += 1
        elif (Move == 1 and x == 3) or (Move == 2 and x == 1) or (Move == 3 and x == 2):
            print("You win")
            M_points += 1
        elif x == Move:
            print("It's a draw")
        print(f"The score is {M_points} to {x_points}.")
        i += 1
print(f"The final score is {M_points} to {x_points}.")
if M_points > x_points:
    print("Great Job, You Win!")
elif M_points < x_points:
    print("LOSER!")
elif M_points == x_points:
    print("It's a draw.")

