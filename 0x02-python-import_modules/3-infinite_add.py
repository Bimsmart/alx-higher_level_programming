#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    s_len = len(sys.argv)
    sum = 0
    if s_len == 1:
        sum == 0
    else:
        for c in range(1, s_len):
            sum += int(sys.argv[c])
    print("{:d}".format(sum))
