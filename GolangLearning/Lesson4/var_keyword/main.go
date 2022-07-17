package main

import "fmt"

// var can be used to declare global variables (variables outside of function scope)
var z = 5
// Initialize a variable num of TYPE in and assigns 0 value
// Unassigned variables are assigned default variable of 0 for the TYPE
var num int 

func main() {
	fmt.Println(num)
	x := 10

	var y = 1

	fmt.Println(x + y + z)
}