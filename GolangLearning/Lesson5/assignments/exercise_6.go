package main

import (
	"fmt"
)

const (
	year1 = 2022 + iota
	year2 = 2022 + iota
	year3 = 2022 + iota
	year4 = 2022 + iota
)

func main() {
	fmt.Printf("Year 1: %d\nYear 2: %d\nYear 3: %d\nYear 4: %d\n", year1, year2, year3, year4)
}