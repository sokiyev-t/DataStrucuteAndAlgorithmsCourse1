"""
Lesson 5: Recursion
Topics:
1) What recursion is
2) Base case and recursive case
3) Grokking-style recursion examples

This file is designed for classroom explanation and live demo.
"""

# def print_greeting(name):
#     result_name=f"Hello, {name}!"
#     return result_name

# name=input("Enter your name: ")

# print_result = print_greeting(name)

# print(print_result);





def countdown(n):
	"""Print numbers from n to 1 using recursion."""
	print(n)
	if n<=1:
		print("Blast off!")
		return
	else:
		countdown(n-1)
	# if n <= 0:
	# 	print("Blast off!")
	# 	return

	# print(n)
	# countdown(n - 1)

countdown(3)

def greet(name):
	"""Small call-stack demo inspired by Grokking Algorithms."""
	print(f"Hello, {name}!")
	greet2(name)
	print("getting ready to say bye...")
	bye()


def greet2(name):
	print(f"How are you, {name}?")


def bye():
	print("ok bye!")


def factorial(n):
	"""
	Factorial using recursion.
	n! = n * (n - 1)!
	Base case: 0! = 1 and 1! = 1
	"""
	if n < 0:
		raise ValueError("factorial is not defined for negative numbers")
	if n <= 1:
		return 1
	return n * factorial(n - 1)


def sum_list_recursive(arr):
	"""Return the sum of a list using recursion."""
	if not arr:
		return 0
	return arr[0] + sum_list_recursive(arr[1:])


def count_items_recursive(arr):
	"""Count list items recursively (like Grokking chapter exercises)."""
	if not arr:
		return 0
	return 1 + count_items_recursive(arr[1:])


def max_recursive(arr):
	"""Find the max element recursively."""
	if not arr:
		raise ValueError("max_recursive requires a non-empty list")
	if len(arr) == 1:
		return arr[0]

	sub_max = max_recursive(arr[1:])
	return arr[0] if arr[0] > sub_max else sub_max


def quicksort(arr):
	"""Classic recursive quicksort from Grokking Algorithms."""
	if len(arr) < 2:
		return arr

	pivot = arr[0]
	less = [x for x in arr[1:] if x <= pivot]
	greater = [x for x in arr[1:] if x > pivot]
	return quicksort(less) + [pivot] + quicksort(greater)


def search_key_in_boxes(boxes):
	"""
	Recursive 'boxes inside boxes' search.
	A box can contain:
	- "key"
	- other strings
	- another list (smaller box)
	"""
	for item in boxes:
		if item == "key":
			return True
		if isinstance(item, list) and search_key_in_boxes(item):
			return True
	return False


def recursive_binary_search(arr, target, left, right):
	"""Return index of target in sorted arr using recursion, else -1."""
	if left > right:
		return -1

	mid = (left + right) // 2

	if arr[mid] == target:
		return mid
	if target < arr[mid]:
		return recursive_binary_search(arr, target, left, mid - 1)
	return recursive_binary_search(arr, target, mid + 1, right)


def explain(title, lines):
	"""Print a clean explanation block."""
	print("=" * 72)
	print(title)
	print("=" * 72)
	for line in lines:
		print(line)
	print()


def main():
	print("RECURSION LESSON")
	print()

	explain(
		"1) IDEA OF RECURSION",
		[
			"- A function calls itself to solve a smaller version of the same problem.",
			"- Every recursive solution needs:",
			"  1) Base case (stopping condition)",
			"  2) Recursive case (move toward the base case)",
		],
	)

	explain(
		"2) COUNTDOWN EXAMPLE",
		[
			"countdown(5) output:",
		],
	)
	countdown(5)
	print()

	explain(
		"3) CALL STACK (GREET EXAMPLE)",
		[
			"This shows function calls stacking and returning in order:",
			"greet('Aisha') -> greet2('Aisha') -> bye()",
		],
	)
	greet("Aisha")
	print()

	explain(
		"4) FACTORIAL EXAMPLE",
		[
			"factorial(5) = 5 * 4 * 3 * 2 * 1 = 120",
			f"Result: {factorial(5)}",
		],
	)

	numbers = [3, 7, 2, 9, 4]
	explain(
		"5) RECURSIVE SUM / COUNT / MAX",
		[
			f"List: {numbers}",
			f"sum_list_recursive(list) = {sum_list_recursive(numbers)}",
			f"count_items_recursive(list) = {count_items_recursive(numbers)}",
			f"max_recursive(list) = {max_recursive(numbers)}",
		],
	)

	unsorted_data = [10, 5, 2, 3]
	explain(
		"6) QUICKSORT (DIVIDE AND CONQUER)",
		[
			f"Unsorted: {unsorted_data}",
			f"Sorted by quicksort: {quicksort(unsorted_data)}",
		],
	)

	boxes = ["book", ["toy", ["coin", "key"]], "pen"]
	explain(
		"7) FINDING A KEY IN NESTED BOXES",
		[
			f"Boxes: {boxes}",
			f"Key found: {search_key_in_boxes(boxes)}",
		],
	)

	sorted_data = [11, 12, 22, 25, 34, 64, 90]
	target = 34
	idx = recursive_binary_search(sorted_data, target, 0, len(sorted_data) - 1)
	explain(
		"8) RECURSIVE BINARY SEARCH",
		[
			f"Sorted list: {sorted_data}",
			f"Target: {target}",
			f"Found at index: {idx}",
		],
	)

	print("Recursion Tips")
	print("- Always write the base case first.")
	print("- Ensure each call gets closer to the base case.")
	print("- Be careful with memory usage for deep recursion.")


if __name__ == "__main__":
	main()
