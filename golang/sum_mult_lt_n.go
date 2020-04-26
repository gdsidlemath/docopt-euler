package main

import (
    "fmt"
    "github.com/docopt/docopt-go"
)

const (
    usage = `
Usage:
    sum_mult_lt_n [-n number] [-j multiple1] [-k multiple2]

Options:
    -n number     number to calculate sum of multiples under [Default: 1000]
    -j multiple1  first number to find multiples of [Default: 3]
    -k multiple2  second number to find multiples of [Default: 5]

Description:
    Project Euler Problem 1: Find the sum of all multiples of 3 or 5 below 1000
`
)

func main() {
    opt, _ := docopt.ParseDoc(usage)
    number, _ := opt.Int("-n")
    multiple1, _ := opt.Int("-j")
    multiple2, _ := opt.Int("-k")
    end_sum := 0
    for i := 1; i < number; i++ {
        if (i % multiple1 == 0 ) || (i % multiple2 == 0) {
            end_sum += i
        }
    }
    fmt.Println(end_sum)
}
