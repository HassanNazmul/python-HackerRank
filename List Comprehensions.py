# Author: Nazmul Hassan
# Submit: HackerRank
# Date: 06/01/2021

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

# Hacker Rank Solution From Here

res = [[i, j, k] for i in range(x+1) for j in range(y+1)
       for k in range(z+1) if i+j+k != n]
print(res)
