#!/usr/bin/env python3

# "Author" Kledis Gjoni
# "Author ID" kgjoni
# "Date Created" 2025/1/20
import sys
if len(sys.argv) != 1:
    timer = int(sys.argv[1])
else:
     timer = 3
while timer != 0:
    print(timer)
    timer = timer - 1
print('blast off!')
