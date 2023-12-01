#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    s_len = len(sys.argv)
    if s_len == 1:
        print("{} arguments".format(s_len - 1))
    elif s_len == 2:
        print("{} argment:".format(s_len - 1)) 
    else:
        print("{} argumens:".format(s_len -1))
    for x in range(1, s_len):
        print("{}: {}".format(x, sys.argv[x]))
