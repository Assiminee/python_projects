"""
Hangman game.
The game has 4 difficulties. You start off by picking a difficulty (1-4). The program randomly picks a word and you have to guess what the word is.
"""
import random

easy = [["c", "a", "t"], ["s", "u", "n"], ["c", "u", "p"], ["b", "o", "o", "k"], ["l", "i", "p", "s"],
        ["w", "o", "r", "m"], ["g", "h", "o", "s", "t"], ["s", "n", "a", "k", "e"], ["s", "w", "i", "n", "g"],
        ["b", "a", "n", "a", "n", "a"], ["f", "l", "o", "w", "e", "r"], ["j", "a", "c", "k", "e", "t"]]

medium = [["b", "e", "a", "c", "h"], ["c", "e", "l", "l", "o"], ["c", "h", "a", "l", "k"],
          ["t", "i", "c", "k", "e", "t"], ["d", "o", "l", "l", "a", "r"], ["c", "a", "m", "e", "r", "a"],
          ["p", "e", "l", "i", "c", "a", "n"], ["r", "a", "i", "n", "b", "o", "w"], ["b", "e", "e", "h", "i", "v", "e"],
          ["b", "l", "o", "w", "f", "i", "s", "h"], ["m", "u", "s", "h", "r", "o", "o", "m"],
          ["d", "o", "g", "h", "o", "u", "s", "e"]]

hard = [["l", "u", "c", "k", "y"], ["a", "b", "y", "s", "s"], ["a", "f", "f", "i", "x"], ["s", "u", "b", "w", "a", "y"],
        ["l", "u", "x", "u", "r", "y"], ["a", "b", "s", "u", "r", "d"], ["l", "e", "n", "g", "t", "h", "s"],
        ["g", "n", "o", "s", "t", "i", "c"], ["f", "u", "c", "h", "s", "i", "a"],
        ["b", "l", "i", "z", "z", "a", "r", "d"], ["g", "l", "o", "w", "w", "o", "r", "m"],
        ["v", "a", "p", "o", "r", "i", "z", "e"]]

real_hard = [["b", "u", "f", "f", "o", "o", "n"], ["j", "a", "y", "w", "a", "l", "k"],
             ["j", "u", "k", "e", "b", "o", "x"], ["f", "i", "s", "h", "h", "o", "o", "k"],
             ["y", "o", "u", "t", "h", "f", "u", "l"], ["w", "h", "e", "e", "z", "i", "n", "g"],
             ["c", "o", "c", "k", "i", "n", "e", "s", "s"], ["b", "u", "z", "z", "w", "o", "r", "d", "s"],
             ["p", "n", "e", "u", "m", "o", "n", "i", "a"], ["s", "t", "r", "o", "n", "g", "h", "o", "l", "d"],
             ["f", "l", "u", "f", "f", "i", "n", "e", "s", "s"], ["z", "i", "g", "z", "a", "g", "g", "i", "n", "g"]]

HANGMANPICS = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''']
tries = len(HANGMANPICS) - 1


def gameplay(count):
    global tries
    string = count[random.randrange(0, 11)]
    for count in string:
        print("_", end="")
    t2 = []
    for count in range(len(string)):
        t2.append("_")
    c = 0
    wc = len(string)
    while wc > 0:
        k = 0
        L = input("\nEnter a letter ")
        t = []
        for count in range(len(string)):
            if L == t2[count]:
                k = 1
                break
            elif L == string[count]:
                c += 1
                t.append(count)
        if c > 0:
            i = 0
            for count in range(len(string)):
                if count == t[i]:
                    t2[count] = L
                    if i < len(t) - 1:
                        i += 1
            print(t2)
        else:
            if k == 1:
                print("You already picked this letter")
            print(HANGMANPICS[tries])
            print(t2)
            if tries > -1:
                tries -= 1
            if tries == -1:
                print("You lose!")
                break
        wc -= c
        if wc == 0:
            print("You guessed the word correctly")
            break
        c = 0


x = int(input("Choose a difficulty level: 1, 2, 3, or 4.\n"))
if x == 1:
    gameplay(easy)
elif x == 2:
    gameplay(medium)
elif x == 3:
    gameplay(hard)
elif x == 4:
    gameplay(real_hard)
else:
    print("You picked the wrong number")
