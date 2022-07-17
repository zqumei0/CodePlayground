package main

import (
	"fmt"
)

func main() {
	num := 16
	fmt.Printf("Decimal: %d\nBinary: %b\nHex: %x\n", num, num, num)
	
	shifted_num := num << 1
	fmt.Printf("Decimal: %d\nBinary: %b\nHex: %x\n", shifted_num, shifted_num, shifted_num)
}