package main

func search(nums []int, target int) int {
	left, right := 0, len(nums)-1
	for left <= right {
		pivot := left + (right-left)/2
		if nums[pivot] == target {
			return pivot
		}
		if target < nums[pivot] {
			right = pivot - 1
		} else {
			left = pivot + 1
		}
	}
	return -1
}
