from __future__ import print_function
import argparse
import time

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('X', type=int,
                help="What is the first number?")
    parser.add_argument('Y', type=int,
                help="What is the second number?")

    args = parser.parse_args()
    X = args.X
    Y = args.Y
    for i in range (0,100) :
        print("%d + %d = %d" % (X, Y, X+Y))
        time.sleep(2) 

if __name__=="__main__":
    main()