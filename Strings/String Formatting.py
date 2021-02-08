# Author: Nazmul Hassan
# Submit: HackerRank
# Date: 08/02/2021

def print_formated(number):
    # Code is Here
    for i in range(1, number + 1):
        width = len(f"{number:b}")
        print(f"{i:{width}} {i:{width}o} {i:{width}X} {i:{width}b}")


if __name__ == '__main__':
    n = int(input())
    print_formated(n)
