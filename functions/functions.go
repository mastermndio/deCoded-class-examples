package main

import "fmt"

func hello(first string, age int) {
	fmt.Printf("Hello %v, you are %v years old", first, age)
}

func main() {
	hello("Aaron", 30)
}
