# Author: Nazmul Hassan
# Submit: HackerRank
# Date: 05/02/2021

# Hacker Rank Solution From Here

N = input().split()
M = input().split()
A = set(input().split())
B = set(input().split())

X = 0

for i in M:
    if i in A:
        X += 1
    if i in B:
        X -= 1

print(X)
