package main

import "fmt"

func main() {
	str := "On"

	if str == "One" {
		fmt.Printf("String to int: 1\n")
	} else if str == "Two" {
		fmt.Printf("String to int: 2\n")
	} else {
		fmt.Printf("Unknown int\n")
	}
}