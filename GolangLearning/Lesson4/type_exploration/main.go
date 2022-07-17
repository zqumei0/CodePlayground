package main

import "fmt"

var REGULAR_STRING string = "This needs all \" to be escaped."
var LITERAL_STRING string = `This does not need any escapes`

var some_int int
var some_string string
var some_bool bool
var some_float float32
var some_float_2 float64

func main() {
	fmt.Println(REGULAR_STRING)
	fmt.Printf("%T\n", REGULAR_STRING)
	fmt.Println(LITERAL_STRING)
	fmt.Printf("%T\n", LITERAL_STRING)

	show_defaults()

	create_new_type()
}

/*
 * Show default values for some primitive types
 */
func show_defaults(){
	fmt.Println(some_int)
	fmt.Println(some_string)
	fmt.Println(some_bool)
	fmt.Println(some_float)
	fmt.Println(some_float_2)
}

func create_new_type() {
	type new_type int

	var new_var new_type = 43
	fmt.Println(new_var)
	fmt.Printf("%T\n", new_var)

	// Converting new_type -> int
	var converted_int int = int(new_var)
	fmt.Printf("%T\n", converted_int)

	var new_type_var new_type = new_type(converted_int)
	fmt.Printf("%T\n", new_type_var)
}