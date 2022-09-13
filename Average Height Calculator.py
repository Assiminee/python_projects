"""Takes a list of heights in cm, converts the heights into integers, calculates then outputs the average height"""

student_heights = input("Input a list of student heights in cm: ").split()

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

x = 0

for n in student_heights:
    x += 1

somme = 0
for n in student_heights:
    somme += n

somme = somme/x
print(f"The average height in this class is: {round(somme)}")
