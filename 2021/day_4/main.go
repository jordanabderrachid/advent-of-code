package main

import (
	"fmt"
	"regexp"
	"strconv"
	"strings"

	"github.com/jordanabderrachid/advent_of_code/2021/common"
)

type cell struct {
	value int
	i, j  int
	drawn bool
}

func (c cell) String() string {
	return fmt.Sprintf("[i: %d, j: %d, v: %d, drawn: %t]", c.i, c.j, c.value, c.drawn)
}

type bingo struct {
	cells []*cell
}

func (b bingo) String() string {
	var sb strings.Builder
	for i, c := range b.cells {
		if i != 0 && i%5 == 0 {
			sb.WriteString("\n")
		}

		sb.WriteString(c.String())
		sb.WriteString("\n")
	}

	return sb.String()
}

func (b *bingo) draw(value int) {
	for _, c := range b.cells {
		if c.value == value {
			c.drawn = true
		}
	}
}

func (b *bingo) won() bool {
	for n := 0; n < 5; n++ {
		line := b.cellsAtLine(n)
		col := b.cellsAtCol(n)
		if onlyDrawn(line) || onlyDrawn(col) {
			return true
		}
	}

	return false
}

func (b *bingo) cellsAtLine(i int) []*cell {
	res := make([]*cell, 0)
	for _, c := range b.cells {
		if c.i == i {
			res = append(res, c)
		}
	}

	return res
}

func (b *bingo) cellsAtCol(j int) []*cell {
	res := make([]*cell, 0)
	for _, c := range b.cells {
		if c.j == j {
			res = append(res, c)
		}
	}

	return res
}

func (b *bingo) sumOfUnmarked() int {
	res := 0
	for _, c := range b.cells {
		if !c.drawn {
			res += c.value
		}
	}

	return res
}

func onlyDrawn(cells []*cell) bool {
	for _, c := range cells {
		if !c.drawn {
			return false
		}
	}
	return true
}

func main() {
	data := common.ReadFile("day_4/input.txt")
	parts := strings.Split(string(data), "\n\n")

	drawRaw := parts[0]
	draw := parseDraw(drawRaw)

	bingosRaw := parts[1:]
	bingos := make([]*bingo, len(bingosRaw))
	for i, bingoRaw := range bingosRaw {
		bingos[i] = parseBingo(bingoRaw)
	}

	// fmt.Println("===== BEFORE =====")
	// for _, b := range bingos {
	// 	fmt.Printf("%s\n", b)
	// }

game:
	for _, v := range draw {
		for _, b := range bingos {
			b.draw(v)
			if b.won() {
				sum := b.sumOfUnmarked()
				fmt.Println(sum * v)
				break game
			}
		}
	}

	// fmt.Println("===== AFTER =====")
	// for _, b := range bingos {
	// 	fmt.Printf("%s\n", b)
	// }
}

func parseDraw(input string) []int {
	parts := strings.Split(input, ",")
	res := make([]int, len(parts))
	for i, p := range parts {
		n, err := strconv.ParseInt(p, 10, 64)
		if err != nil {
			panic(fmt.Sprintf("failed to parse int: %s err=%s\n", p, err.Error()))
		}

		res[i] = int(n)
	}

	return res
}

func parseBingo(input string) *bingo {
	cells := make([]*cell, 0)
	lines := strings.Split(input, "\n")
	for i, line := range lines {
		columns := parseLine(line)
		for j, valueRaw := range columns {
			value, err := strconv.ParseInt(valueRaw, 10, 64)
			if err != nil {
				panic(fmt.Sprintf("failed to parse int: %s  %s err=%s\n", valueRaw, line, err.Error()))
			}
			cells = append(cells, &cell{
				value: int(value), i: i, j: j, drawn: false,
			})
		}
	}

	return &bingo{cells: cells}
}

func parseLine(line string) []string {
	parser := regexp.MustCompile(`^(.{2})\s(.{2})\s(.{2})\s(.{2})\s(.{2})$`)
	found := parser.FindAllStringSubmatch(line, -1)

	res := make([]string, len(found[0][1:]))
	for i, v := range found[0][1:] {
		res[i] = strings.TrimSpace(v)
	}

	return res
}
