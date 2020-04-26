#include "docopt.h"

#include <iostream>
#include <string>

static const char USAGE[]=
R"(
    Usage:
        helloworld [-n name]

    Options:
        -n name  name to output [default: World]

    Description:
        Basic C++ program

)";

int main(int argc, const char** argv) {
    std::map<std::string, docopt::value> args = docopt::docopt(USAGE,
                                                    { argv + 1, argv + argc},
                                                    true,
                                                    "Hello World program 0.1");

    std::string output = "Hello " + args["-n"].asString() + "!";
    std::cout << output << std::endl;
    return 0;
}

