"""
Lesson 3: Binary Search

Binary search works only on a sorted list.
Time complexity: O(log n)
"""


def binary_search(arr, target):
	"""Return index of target in sorted arr, or -1 if not found."""
	left = 0
	right = len(arr) - 1

	while left <= right:
		mid = (left + right) // 2

		if arr[mid] == target:
			return mid
		if arr[mid] < target:
			left = mid + 1
		else:
			right = mid - 1

	return -1


if __name__ == "__main__":
	numbers = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]

	target_1 = 23
	result_1 = binary_search(numbers, target_1)
	print(f"Searching for {target_1}: index = {result_1}")

	target_2 = 7
	result_2 = binary_search(numbers, target_2)
	print(f"Searching for {target_2}: index = {result_2}")

