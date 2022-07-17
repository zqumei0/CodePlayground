package main

import (
	"fmt"
)

const untyped_const = 10
const typed_const int8 = 12

func main() {
	fmt.Printf("Untyped Constant: %d\n", untyped_const)
	fmt.Printf("Typed Constant: %d\n", typed_const)
}