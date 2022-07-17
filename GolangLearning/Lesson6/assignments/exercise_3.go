package main

import "fmt"

func main() {
	start_year := 2000

	for start_year < 2022 {
		fmt.Println(start_year)
		start_year++
	}
}