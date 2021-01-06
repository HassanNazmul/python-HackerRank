# Author: Nazmul Hassan
# Submit: HackerRank
# Date: 06/01/2021

def is_leap(year):
    leap = False

    # # Hacker Rank Logicm is here

    if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
        leap = True

    return leap


year = int(input())
print(is_leap(year))
