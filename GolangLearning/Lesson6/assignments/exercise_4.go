package main

import "fmt"

func main() {
	start_year := 2000

	for {
		if start_year > 2022 {
			break
		}

		fmt.Println(start_year)
		start_year++
	}
}