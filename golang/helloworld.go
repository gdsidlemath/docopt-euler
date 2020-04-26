package main

import (
    "fmt"
    "github.com/docopt/docopt-go"
)

const (
    usage = `
Usage:
    helloworld [-n name]

Options:
    -n name  name to output

Description:
    Basic golang program
`
)

func main(){
    opt, _ := docopt.ParseDoc(usage)
    name, _ := opt.String("-n")
    fmt.Println("Hello " + name + "!")
}
