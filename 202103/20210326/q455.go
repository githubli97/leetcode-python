package main

import "sort"

func findContentChildren(g []int, s []int) int {
	sort.Ints(g)
	sort.Ints(s)
	result := 0

	gIndex := 0
	for _, item := range s {
		if gIndex == len(g) {
			break
		}
		if g[gIndex] <= item {
			result++
			gIndex++
		}
	}
	return result
}
