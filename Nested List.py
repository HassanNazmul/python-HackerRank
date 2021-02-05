# Author: Nazmul Hassan
# Submit: HackerRank
# Date: 05/02/2021

Student = []
Second_Lowest_Grade = []
Grade = set()

if __name__ == "__main__":
    for _ in range(int(input())):
        name = input()
        score = float(input())
        Student.append([name, score])
        Grade.add(score)

# Hacker Rank Solution From Here


Second_Lowest = sorted(Grade)[1]

for name, score in Student:
    if score == Second_Lowest:
        Second_Lowest_Grade.append(name)

for name in sorted(Second_Lowest_Grade):
    print(name, end="\n")
