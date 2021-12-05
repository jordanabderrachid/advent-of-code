package main

import (
	"fmt"
	"strings"

	"github.com/jordanabderrachid/advent_of_code/2021/common"
)

type bitSet []bool

func main() {
	data := common.ReadFile("day_3/input.txt")
	// 	data := []byte(`00100
	// 11110
	// 10110
	// 10111
	// 10101
	// 01111
	// 00111
	// 11100
	// 10000
	// 11001
	// 00010
	// 01010`)
	raw := common.ConvertToStringSlice(data)
	bitSets := make([]bitSet, len(raw))
	for i, e := range raw {
		bitSets[i] = convertToBitSet(e)
	}

	oxy := findOxigenGeneratorRating(bitSets)
	fmt.Println(oxy)
	co2 := findCO2ScrubberRating(bitSets)
	fmt.Println(co2)
	fmt.Println(oxy * co2)
	// bitSetLen := len(bitSets[0])
	// mostPopularBits := make(bitSet, bitSetLen)
	// for i := 0; i < bitSetLen; i++ {
	// 	mostPopularBits[i] = mostPopularBitAt(i, bitSets)
	// }

	// gamma := bitSetToInt(mostPopularBits)
	// epsilon := bitSetToInt(invert(mostPopularBits))
	// fmt.Println(gamma * epsilon)
}

func convertToBitSet(raw string) bitSet {
	parts := strings.Split(raw, "")

	res := make([]bool, len(parts))
	for i, val := range parts {
		if val == "1" {
			res[i] = true
		} else {
			res[i] = false
		}
	}

	return res
}

func mostPopularBitAt(i int, bitSets []bitSet, tieBreak bool) bool {
	ones := 0
	zeros := 0

	for _, bitSet := range bitSets {
		if bitSet[i] {
			ones++
		} else {
			zeros++
		}
	}

	if ones == zeros {
		return tieBreak
	}

	return ones > zeros
}

func leastPopularBitAt(i int, bitSets []bitSet, tieBreak bool) bool {
	ones := 0
	zeros := 0

	for _, bitSet := range bitSets {
		if bitSet[i] {
			ones++
		} else {
			zeros++
		}
	}

	if ones == zeros {
		return tieBreak
	}

	if ones > zeros {
		return false
	}

	return true
}

func bitSetToInt(bitSet bitSet) (res int) {
	for _, bit := range bitSet {
		res = res << 1
		if bit {
			res += 1
		}
	}
	return
}

// func invert(bs bitSet) (inverted bitSet) {
// 	inverted = make(bitSet, len(bs))
// 	for i, b := range bs {
// 		inverted[i] = !b
// 	}

// 	return
// }

func filter(bitSets []bitSet, i int, bit bool) []bitSet {
	res := make([]bitSet, 0)

	for _, bs := range bitSets {
		if bs[i] == bit {
			res = append(res, bs)
		}
	}

	return res
}

func findOxigenGeneratorRating(bitSets []bitSet) int {
	bitSetLen := len(bitSets[0])
	for i := 0; i < bitSetLen; i++ {
		mostPopularBit := mostPopularBitAt(i, bitSets, true)
		bitSets = filter(bitSets, i, mostPopularBit)
	}

	if len(bitSets) != 1 {
		panic("too many bitsets remaining")
	}

	return bitSetToInt(bitSets[0])
}

func findCO2ScrubberRating(bitSets []bitSet) int {
	bitSetLen := len(bitSets[0])
	for i := 0; i < bitSetLen; i++ {
		leastPopularBit := leastPopularBitAt(i, bitSets, false)
		bitSets = filter(bitSets, i, leastPopularBit)

		if len(bitSets) == 1 {
			break
		}
	}

	if len(bitSets) != 1 {
		panic(fmt.Sprintf("too many bitsets remaining %d", len(bitSets)))
	}

	return bitSetToInt(bitSets[0])
}
