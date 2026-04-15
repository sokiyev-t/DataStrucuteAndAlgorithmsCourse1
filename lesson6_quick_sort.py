# def sum(arr):
#     """Helper function to sum a list, used in some examples."""
#     total = 0
#     for num in arr:
#         total += num
#     return total

# s=sum([1, 2, 3, 4])
# print(f'Sum: {s}')  # Should print 10


# def recursive_sum(arr):
#     """Recursive version of sum."""
#     if not arr:
#         return 0
#     return arr[0] + recursive_sum(arr[1:])


# ar=[1, 2, 3, 4]

# rs=recursive_sum(ar)


# print(ar[1:])  # Should print [2, 3, 4]

# print(f'Recursive Sum: {rs}')  # Should print 10


"""
Lesson 6: Quick Sort
Topics:
1) Divide and conquer review
2) Pivot and partition
3) Grokking-style recursive quick sort
4) In-place quick sort (advanced)
5) Time complexity discussion

This file is designed for classroom explanation and live demo.
"""


def quick_sort(arr):
	"""
	Grokking Algorithms style quick sort (not in-place):
	- Base case: lists with 0 or 1 element are already sorted.
	- Recursive case:
	  1) Choose a pivot
	  2) Partition into less/equal/greater
	  3) Recursively sort less and greater

	Time Complexity:
	- Best/Average: O(n log n)
	- Worst: O(n^2) (for repeatedly bad pivots)

	Space Complexity:
	- This version creates new lists, so it uses extra memory.
	"""
	if len(arr) < 2:
		return arr[:]

	pivot = arr[0]
	less = [x for x in arr[1:] if x <= pivot]
	greater = [x for x in arr[1:] if x > pivot]

	return quick_sort(less) + [pivot] + quick_sort(greater)


arr=[7,10, 5, 2, 3]
sorted_arr=quick_sort(arr)
print(f'Input: {arr}')
print(f'Sorted: {sorted_arr}')


def quick_sort_trace(arr, depth=0):
	"""Trace recursive calls so students can see divide-and-conquer in action."""
	indent = "  " * depth
	print(f"{indent}quick_sort({arr})")

	if len(arr) < 2:
		print(f"{indent}return {arr}")
		return arr[:]

	pivot = arr[0]
	less = [x for x in arr[1:] if x <= pivot]
	greater = [x for x in arr[1:] if x > pivot]

	print(f"{indent}pivot = {pivot}")
	print(f"{indent}less = {less}")
	print(f"{indent}greater = {greater}")

	sorted_less = quick_sort_trace(less, depth + 1)
	sorted_greater = quick_sort_trace(greater, depth + 1)

	result = sorted_less + [pivot] + sorted_greater
	print(f"{indent}combined -> {result}")
	return result


def partition_lomuto(arr, low, high):
	"""Partition helper for in-place quick sort (Lomuto scheme)."""
	pivot = arr[high]
	i = low - 1

	for j in range(low, high):
		if arr[j] <= pivot:
			i += 1
			arr[i], arr[j] = arr[j], arr[i]

	arr[i + 1], arr[high] = arr[high], arr[i + 1]
	return i + 1


def quick_sort_inplace(arr, low=0, high=None):
	"""
	Advanced quick sort: sorts the same list in-place.
	Useful to compare with the Grokking version that creates new lists.
	"""
	if high is None:
		high = len(arr) - 1

	if low < high:
		pivot_index = partition_lomuto(arr, low, high)
		quick_sort_inplace(arr, low, pivot_index - 1)
		quick_sort_inplace(arr, pivot_index + 1, high)


def explain(title, lines):
	"""Print a clean explanation block."""
	print("=" * 72)
	print(title)
	print("=" * 72)
	for line in lines:
		print(line)
	print()


def main():
	print("LESSON 6: QUICK SORT")
	print()

	explain(
		"1) LESSON GOAL",
		[
			"By the end of class, students should be able to:",
			"- Explain divide and conquer using quick sort",
			"- Implement Grokking-style quick sort from memory",
			"- Describe why pivot choice affects performance",
		],
	)

	explain(
		"2) QUICK IDEA (GROKKING STYLE)",
		[
			"Step 1: Pick a pivot",
			"Step 2: Put smaller/equal values on one side, larger on the other",
			"Step 3: Recursively sort both sides",
			"Step 4: Combine: sorted_left + pivot + sorted_right",
		],
	)

	data = [10, 5, 2, 3]
	sorted_data = quick_sort(data)
	explain(
		"3) BASIC DEMO",
		[
			f"Input : {data}",
			f"Output: {sorted_data}",
		],
	)

	explain(
		"4) TRACE DEMO (USE THIS LIVE IN CLASS)",
		[
			"Watch how each recursive call makes the problem smaller.",
		],
	)
	quick_sort_trace(data)
	print()

	data_with_duplicates = [6, 3, 6, 2, 9, 6, 1]
	explain(
		"5) DUPLICATES EXAMPLE",
		[
			f"Input : {data_with_duplicates}",
			f"Output: {quick_sort(data_with_duplicates)}",
		],
	)

	already_sorted = [1, 2, 3, 4, 5, 6, 7]
	reversed_data = [7, 6, 5, 4, 3, 2, 1]
	explain(
		"6) COMPLEXITY TALK TRACK",
		[
			"Average case: O(n log n)",
			"Worst case: O(n^2) when pivot choices are repeatedly poor",
			f"Already sorted input example: {already_sorted}",
			f"Reverse sorted input example: {reversed_data}",
			"Ask students: what pivot rule can reduce worst-case risk?",
		],
	)

	inplace_data = [9, 4, 7, 3, 10, 5]
	quick_sort_inplace(inplace_data)
	explain(
		"7) ADVANCED: IN-PLACE QUICK SORT",
		[
			"This version modifies the same list instead of creating new ones.",
			f"In-place sorted output: {inplace_data}",
		],
	)

	print("Practice Tasks")
	print("1) Modify quick_sort to use middle element as pivot.")
	print("2) Count how many recursive calls happen for each input list.")
	print("3) Compare quick sort and selection sort on list length 20.")
	print("4) Explain why base case is required in one sentence.")


if __name__ == "__main__":
	main()
