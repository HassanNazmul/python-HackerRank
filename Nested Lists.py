# Author: Nazmul Hassan
# Submit: HackerRank
# Date: 06/01/2021

dic = {}
marks = {}

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())

# Hacker Rank Solution From Here

dic += [[name, score]]
marks += [score]

sl = (sorted(set(marks)))[1]
for i, j in sorted(dic):
    if j == sl:
        print(i)
