#!/usr/bin/env ruby
require "docopt"
require "pp"

doc = <<DOCOPT
Usage:
    helloworld [-n name]

Options:
    -n name   name to output [default: World]

Description:
    Basic Ruby program
DOCOPT

begin
    args = Docopt::docopt(doc)
rescue Docopt::Exit => e
    puts e.message
end

puts "Hello #{args['-n']}!"

