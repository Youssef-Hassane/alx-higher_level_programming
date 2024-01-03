#!/usr/bin/python3

for index_1 in range(10):
    for index_2 in range(index_1 + 1, 10):
        print("{:d}{:d}".format(index_1, index_2),
              end=(", " if index_1 < 8 or index_2 < 9 else "\n"))
