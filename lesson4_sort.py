"""
Lesson 4: Sorting Algorithms
Topics:
1) Bubble Sort
2) Selection Sort
3) Quick Sort

This file is designed for classroom explanation and live demo.
"""


def bubble_sort(arr):
	"""
	Bubble Sort:
	- Compare neighboring elements.
	- Swap if they are in the wrong order.
	- After each pass, the largest unsorted element moves to the end.

	Time Complexity:
	- Worst/Average: O(n^2)
	- Best (already sorted with early stop): O(n)
	Space Complexity: O(1)
	"""
	a = arr[:]  # Copy so original list stays unchanged
	n = len(a)

	for i in range(n):
		swapped = False
		for j in range(0, n - 1 - i):
			if a[j] > a[j + 1]:
				a[j], a[j + 1] = a[j + 1], a[j]
				swapped = True

		# If no swap happened, list is already sorted.
		if not swapped:
			break

	return a


def selection_sort(arr):
	"""
	Selection Sort:
	- Find the smallest element in the unsorted part.
	- Swap it with the first unsorted position.
	- Repeat by moving the boundary of sorted part.

	Time Complexity:
	- Worst/Average/Best: O(n^2)
	Space Complexity: O(1)
	"""
	a = arr[:]
	n = len(a)

	for i in range(n):
		min_index = i

		for j in range(i + 1, n):
			if a[j] < a[min_index]:
				min_index = j

		a[i], a[min_index] = a[min_index], a[i]

	return a


def quick_sort(arr):
	"""
	Quick Sort (recursive version with extra lists):
	- Choose a pivot.
	- Split into three parts:
	  left  -> values smaller than pivot
	  mid   -> values equal to pivot
	  right -> values greater than pivot
	- Recursively sort left and right, then combine.

	Time Complexity:
	- Best/Average: O(n log n)
	- Worst (bad pivot repeatedly): O(n^2)
	Space Complexity:
	- O(log n) recursion stack average + extra lists in this version
	"""
	if len(arr) <= 1:
		return arr[:]

	pivot = arr[len(arr) // 2]
	left = [x for x in arr if x < pivot]
	mid = [x for x in arr if x == pivot]
	right = [x for x in arr if x > pivot]

	return quick_sort(left) + mid + quick_sort(right)


def explain_and_demo(name, sorter, sample):
	"""Print a neat explanation block and run one demo."""
	print("=" * 72)
	print(name)
	print("=" * 72)
	print(f"Input : {sample}")
	result = sorter(sample)
	print(f"Output: {result}")
	print()


def main():
	print("SORTING ALGORITHMS LESSON")
	print()

	data = [64, 25, 12, 22, 11, 90, 34]

	print("Original list:", data)
	print()

	explain_and_demo("1) BUBBLE SORT", bubble_sort, data)
	explain_and_demo("2) SELECTION SORT", selection_sort, data)
	explain_and_demo("3) QUICK SORT", quick_sort, data)

	print("Comparison Summary")
	print("- Bubble Sort   : simple, many swaps, O(n^2)")
	print("- Selection Sort: simple, fewer swaps, O(n^2)")
	print("- Quick Sort    : usually fastest in practice, O(n log n) average")


if __name__ == "__main__":
	main()
