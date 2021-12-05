package common

import "strings"

func ConvertToStringSlice(data []byte) []string {
	return strings.Split(strings.TrimSpace(string(data)), "\n")
}
