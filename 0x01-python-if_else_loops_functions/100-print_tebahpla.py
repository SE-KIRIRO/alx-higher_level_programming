#!/usr/bin/python3
"""Print the alphabet in reverse order alterning upper and lower case"""
i = 0
for c in range(ord('z'), (ord('a') - 1), -1):
    print(f"{chr(c - i)}", end="")
    if i == 0:
        i = 32
    else:
        i = 0
