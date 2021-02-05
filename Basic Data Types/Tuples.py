# Author: Nazmul Hassan
# Submit: HackerRank
# Date: 05/02/2021

if __name__ == "__main__":
    n = int(input())
    integer_list = map(int, input().split())

# Hacker Rank Solution From Here

t = tuple(integer_list)
print(hash(t))