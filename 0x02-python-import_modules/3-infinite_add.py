#!/usr/bin/python3

import sys
sum = 0
num = sys.argv[1:]
num_count= len(num)

for x in range(num_count):
    sum = sum + int(num[x])
if __name__ == '__main__':
    print(sum)
