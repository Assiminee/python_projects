"""
Password Generator Project
Inputs: number of letters, number of symbols, and number of numbers.
Output: randomly generated password
"""

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
l = int(input("How many letters would you like in your password?\n"))
s = int(input(f"How many symbols would you like?\n"))
n = int(input(f"How many numbers would you like?\n"))
p = []
for x in range(0,l):
    p.append(letters[random.randint(0,25)])
for x in range(0, s):
    p.append(symbols[random.randint(0, 8)])
for x in range(0, n):
    p.append(numbers[random.randint(0, 9)])

random.shuffle(p)
for x in p:
    print(x,end="")


