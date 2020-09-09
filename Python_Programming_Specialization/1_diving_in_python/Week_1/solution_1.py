import sys

num = int(sys.argv[1])

for i in range(num):
    print(' '*(num-i-1)+'#'*(i+1))
