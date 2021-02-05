# Author: Nazmul Hassan
# Submit: HackerRank
# Date: 05/02/2021

if __name__ == "__main__":
    N = int(input())
    Store = []

# Hacker Rank Solution From Here

while N != 0:
    A = input().split()

    if len(A) == 3:
        B = int(A[1])
        C = int(A[2])
    elif len(A) == 2:
        B = int(A[1])

    if A[0] == "insert":
        Store.insert(B, C)
    elif A[0] == "print":
        print(Store)
    elif A[0] == "remove":
        Store.remove(B)
    elif A[0] == "append":
        Store.append(B)
    elif A[0] == "sort":
        Store.sort()
    elif A[0] == "pop":
        Store.pop()
    elif A[0] == "reverse":
        Store.reverse()
    N -= 1
