# Author: Nazmul Hassan
# Submit: HackerRank
# Date: 20/01/2021

def count_substring(string, sub_string):
    # Hacker Rank Solution From Here

    c=0
    l=len(sub_string)
    for i  in range(len(string)):
        s=string[i:i+l]
        if s==sub_string:
            c+=1
    return c

if __name__ == '__main__':