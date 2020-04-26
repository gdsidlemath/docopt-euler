#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Usage:
    sum_mult_lt_n [-n number] [-j multiple1] [-k multiple2]

Options:
    -n number     number to calculate sum of multiples under [default: 1000]
    -j multiple1  first number to find multiples of [default: 3]
    -k multiple2  second number to find multiples of [default: 5]

Description:
    Project Euler Problem 1: Find the sum of all multiples of 3 or 5 below 1000
"""
from docopt import docopt


def main():
    args = docopt(__doc__)
    number = int(args["-n"])
    multiple1 = int(args["-j"])
    multiple2 = int(args["-k"])
    end_sum = 0
    for i in range(number):
        if i % multiple1 == 0 or i % multiple2 ==0:
            end_sum += i
    print(end_sum)

if __name__ == "__main__":
    main()
