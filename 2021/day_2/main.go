package main

import (
	"fmt"
	"strconv"
	"strings"

	"github.com/jordanabderrachid/advent_of_code/2021/common"
)

type direction int

const (
	forward direction = iota
	down
	up
)

func (d direction) String() string {
	switch d {
	case forward:
		return "forward"
	case down:
		return "down"
	case up:
		return "up"
	}

	return "brrrr"
}

type command struct {
	direction direction
	amount    int
}

func (c command) String() string {
	return fmt.Sprintf("%s %d", c.direction, c.amount)
}

func main() {
	data := common.ReadFile("day_2/input.txt")
	// 	data := []byte(`forward 5
	// down 5
	// forward 8
	// up 3
	// down 8
	// forward 2`)
	rawCommands := common.ConvertToStringSlice(data)

	commands := make([]command, len(rawCommands))
	for i, raw := range rawCommands {
		commands[i] = parseCommand(raw)
	}

	pos, depth := navigate(commands)
	fmt.Println(pos * depth)
}

func parseCommand(raw string) command {
	parts := strings.Split(raw, " ")
	if len(parts) != 2 {
		panic(fmt.Sprintf("unexpected command: %s", raw))
	}

	amount, err := strconv.ParseInt(parts[1], 10, 64)
	if err != nil {
		panic(fmt.Sprintf("unexpected command: %s", raw))
	}

	return command{
		direction: parseDirection(parts[0]),
		amount:    int(amount),
	}
}

func parseDirection(raw string) direction {
	switch raw {
	case "forward":
		return forward
	case "down":
		return down
	case "up":
		return up
	}

	panic(fmt.Sprintf("invalid direction %s", raw))
}

func navigate(commands []command) (pos, depth int) {
	aim := 0
	for _, c := range commands {
		switch c.direction {
		case forward:
			pos += c.amount
			depth += aim * c.amount
		case down:
			aim += c.amount
		case up:
			aim -= c.amount
		}
	}

	return
}
