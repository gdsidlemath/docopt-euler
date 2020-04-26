#include "docopt.h"

#include <iostream>
#include <string>

static const char USAGE[] =
R"(
    Usage:
        sum_mult_lt_n [-n number] [-j multiple1] [-k multiple2]

    Options:
        -n number     number to calculate the sum of multiples under [default: 1000]
        -j multiple1  first number to find multiples of [default: 3]
        -k multiple2  second number to find multiples of [default: 5]

    Description:
        Project Euler Problem 1: Find the sum of all multiples of 3 or 5 below 1000

)";

int main(int argc, const char** argv) {
    std::map<std::string, docopt::value> args = docopt::docopt(USAGE,
                                                    { argv + 1, argv + argc},
                                                    true,
                                                    "Sum of Multiples Less Than N 0.1");
    int number = std::stoi(args["-n"].asString());
    int multiple1 = std::stoi(args["-j"].asString());
    int multiple2 = std::stoi(args["-k"].asString());
    int end_sum = 0;
    for(int i=1; i<number; i++) {
        if( i % multiple1 == 0 || i % multiple2 == 0){
            end_sum += i;
        }
    }
    std::cout << end_sum << std::endl;
    return 0;
}

