package main

import "fmt"

func main() {
	favSport := "Football"

	switch favSport{
	case "Football":
		fmt.Printf("Favorite Sport is %s.\n", favSport)
	case "Frisbee":
		fmt.Printf("Favorite Sport is %s.\n", favSport)
	case "Soccer":
		fmt.Printf("Favorite Sport is %s.\n", favSport)
	default:
		fmt.Printf("Unknown Sport.\n")
	}
}