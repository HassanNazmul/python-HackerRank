# Author: Nazmul Hassan
# Submit: HackerRank
# Date: 06/01/2021

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

# Hacker Rank Solution From Here

arr.sort()
print(arr[(arr.index(max(arr)))-1])
