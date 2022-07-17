package main

import "fmt"

func main() {
	/*
	 * := used for initial declaration
	 * Once initialized = can be used for reassignment
	 */
	x := 10
	fmt.Println(x)

	x = 10 + 1
	fmt.Println(x)

	y := x + 4
	fmt.Println(y)
}
