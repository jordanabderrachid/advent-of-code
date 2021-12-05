package common

import (
	"fmt"
	"os"
)

func ReadFile(path string) []byte {
	data, err := os.ReadFile(path)
	if err != nil {
		panic(fmt.Sprintf("failed to read file %s: %s", path, err))
	}

	return data
}
