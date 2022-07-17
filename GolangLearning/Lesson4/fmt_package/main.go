package main

import "fmt"

var x = 10

func main() {
	fmt.Println(x)
	// Type
	fmt.Printf("%T\n", x)
	// Binary
	fmt.Printf("%b\n", x)
	// Hex
	fmt.Printf("%x\n", x)
	// Hex in 0x format
	fmt.Printf("%#x\n", x)
}