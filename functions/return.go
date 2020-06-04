package main

import "fmt"

func addNums(num1 int, num2 int) int {
	sum := num1 + num2
	return sum
}

func main() {
	fmt.Println(addNums(5, 4))
}
