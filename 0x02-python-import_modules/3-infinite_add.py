#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args = len(argv) - 1
    sum = 0
    if args is 0:
        print("{:d}".format(0))
    else:
        for i in range(1, len(argv)):
            sum += int(argv[i])
        print("{:d}".format(sum))
