# Author: Nazmul Hassan
# Submit: HackerRank
# Date: 05/02/2021

# Hacker Rank Solution From Here

def merge_the_tools(string, k):
    # your code goes here
    x = [string[i:i + k] for i in range(0, len(string), k)]

    for i in x:
        j = 0
        short = ""
        for _ in i:
            if i.index(_) == j:
                short += _
            j += 1
        print(short)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
