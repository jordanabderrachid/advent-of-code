package main

import (
	"fmt"
	"strconv"

	"github.com/jordanabderrachid/advent_of_code/2021/common"
)

func main() {
	data := common.ReadFile("day_1/input_part_1.txt")
	input := stringsToInt(common.ConvertToStringSlice(data))
	fmt.Println(countIncrement(input))
	fmt.Println(countSlidingWindowIncrement(input))
}

func stringsToInt(input []string) []int64 {
	res := make([]int64, len(input))

	for i, s := range input {
		conv, err := strconv.ParseInt(s, 10, 64)
		if err != nil {
			panic(fmt.Sprintf("warn: failed to convert string %s to int64: %s\n", s, err.Error()))
		}

		res[i] = conv
	}

	return res
}

func countIncrement(input []int64) int {
	res := 0
	for i := 1; i < len(input); i++ {
		if input[i] > input[i-1] {
			res++
		}
	}

	return res
}

func windowSumAt(i int, input []int64) int64 {
	return input[i-2] + input[i-1] + input[i]
}

func countSlidingWindowIncrement(input []int64) int {
	res := 0
	for i := 3; i < len(input); i++ {
		if windowSumAt(i, input) > windowSumAt(i-1, input) {
			res++
		}
	}

	return res
}
