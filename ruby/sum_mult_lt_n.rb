#!/usr/bin/env ruby
require "docopt"
require "pp"

doc = <<DOCOPT
Usage:
    sum_mult_lt_n [-n number] [-j multiple1] [-k multiple2]

Options:
    -n number     number to calculate sum of multiples under [default: 1000]
    -j multiple1  first number to find multiples of [default: 3]
    -k multiple2  second number to find multiples of [default: 5]

Description:
    Project Euler Problem 1: Find the sum of all multiples of 3 or 5 below 1000
DOCOPT

begin
    args = Docopt::docopt(doc)
rescue Docopt::Exit => e
    puts e.message
end

$number = Integer(args["-n"])
$multiple1 = Integer(args["-j"])
$multiple2 = Integer(args["-k"])
$end_sum = 0
for i in 1..($number-1)
    if i % $multiple1 == 0 || i % $multiple2 == 0
        $end_sum += i
    end
end
puts $end_sum

