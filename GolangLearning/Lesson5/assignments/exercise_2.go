package main

import (
	"fmt"
)

const bigger_num = 12
const smaller_num = 10

func main() {
	eq_result := bigger_num == smaller_num
	le_result := bigger_num <= smaller_num
	ge_result := bigger_num >= smaller_num
	ne_result := bigger_num != smaller_num
	lt_result := bigger_num < smaller_num
	gt_result := bigger_num > smaller_num

	fmt.Printf("Equal: %t\n", eq_result)
	fmt.Printf("Less than or equal to: %t\n", le_result)
	fmt.Printf("Greater than or equal to: %t\n", ge_result)
	fmt.Printf("Not equal: %t\n", ne_result)
	fmt.Printf("Less than: %t\n", lt_result)
	fmt.Printf("Greater than: %t\n", gt_result)
}