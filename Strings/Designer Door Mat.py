# Author: Nazmul Hassan
# Submit: HackerRank
# Date: 05/02/2021

# Hacker Rank Solution From Here

N, M = map(int, input().split())

for i in range(int(N / 2)):
    string = ".|." + (2 * i + 1)
    x = string.center(M, "-")
    print(x)

print("WELCOME".center(M, "-"))

for i in reversed(range(int(N / 2))):
    string = ".|." * (2 * i + 1)
    x = string.center(M, "-")
    print(x)