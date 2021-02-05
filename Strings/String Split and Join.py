# Author: Nazmul Hassan
# Submit: HackerRank
# Date: 05/02/2021

# Hacker Rank Solution From Here


def split_and_join(line):
    # write your code here

    line = line.split(" ")
    line = "-".join(line)

    return line


if __name__ == "__main__":
    line = input()
    result = split_and_join(line)
    print(result)