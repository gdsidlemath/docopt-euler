#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Usage:
    helloworld [-n name]

Options:
    -n name     name to output [default: World]

Description:
    Basic python program
"""
from docopt import docopt


def main():
    args = docopt(__doc__)
    name = args["-n"]
    print("Hello " + name + "!")

if __name__ == "__main__":
    main()
