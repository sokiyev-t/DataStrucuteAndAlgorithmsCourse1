# ============================================================================
# LOGIC OPERATIONS, LOOPS, AND ARRAYS - TEACHING EXAMPLES
# ============================================================================

print("=" * 70)
print("PART 1: LOGIC OPERATIONS (and, or, not)")
print("=" * 70)

# --- AND Operation ---
print("\n1. AND Operation (both conditions must be True)")
print("-" * 50)

age = 18
has_license = True


# Example 1: Checking if someone can drive
if age >= 18 and has_license:
    print(f"Age: {age}, License: {has_license} → CAN DRIVE ✓")
else:
    print(f"Age: {age}, License: {has_license} → CANNOT DRIVE ✗")

# Example with False result
age = 16
if age >= 18 and has_license:
    print(f"Age: {age}, License: {has_license} → CAN DRIVE ✓")
else:
    print(f"Age: {age}, License: {has_license} → CANNOT DRIVE ✗")

# --- OR Operation ---
print("\n2. OR Operation (at least one condition must be True)")
print("-" * 50)

day = "Saturday"
is_holiday = False

# Example: When can I relax?
if day == "Saturday" or day == "Sunday" or is_holiday:
    print(f"Day: {day}, Holiday: {is_holiday} → TIME TO RELAX! 🎉")
else:
    print(f"Day: {day}, Holiday: {is_holiday} → WORK TIME 💼")

day = "Monday"
is_holiday = True
if day == "Saturday" or day == "Sunday" or is_holiday:
    print(f"Day: {day}, Holiday: {is_holiday} → TIME TO RELAX! 🎉")
else:
    print(f"Day: {day}, Holiday: {is_holiday} → WORK TIME 💼")

# --- NOT Operation ---
print("\n3. NOT Operation (reverses the boolean value)")
print("-" * 50)

is_raining = False

if not is_raining:
    print(f"Is raining: {is_raining} → Go for a picnic! ☀️")
else:
    print(f"Is raining: {is_raining} → Stay at home 🏠")

is_raining = True
if not is_raining:
    print(f"Is raining: {is_raining} → Go for a picnic! ☀️")
else:
    print(f"Is raining: {is_raining} → Stay at home 🏠")

# --- Complex Logic ---
print("\n4. Complex Logic (combining AND, OR, NOT)")
print("-" * 50)

score = 75
attendance = 85
behavior = "good"

# Can a student pass the class?
if (score >= 60 and attendance >= 75) and (not behavior == "bad"):
    print(f"Score: {score}, Attendance: {attendance}, Behavior: {behavior}")
    print("→ STUDENT PASSED ✓")
else:
    print(f"Score: {score}, Attendance: {attendance}, Behavior: {behavior}")
    print("→ STUDENT FAILED ✗")

print("\n" + "=" * 70)
print("PART 2: LOOPS")
print("=" * 70)

# --- FOR Loop ---
print("\n5. FOR Loop (iterate a specific number of times)")
print("-" * 50)

print("Counting from 1 to 5:")
for i in range(1, 6):
    print(f"Number: {i}")

print("\nMultiplication table (5 times table):")
for i in range(1, 10):
    print(f"5 × {i} = {5 * i}")

# --- FOR Loop with List ---
print("\n6. FOR Loop with List (iterate through items)")
print("-" * 50)

fruits = ["apple", "banana", "orange", "grape", "mango"]
print(f"Fruits list: {fruits}")

print("\nIterating through fruits:")
for fruit in fruits:
    print(f"  - {fruit.capitalize()}")

print("\nIterating with index:")
for index, fruit in enumerate(fruits):
    print(f"  Position {index}: {fruit}")

# --- WHILE Loop ---
print("\n7. WHILE Loop (repeat while condition is True)")
print("-" * 50)

print("Countdown from 5 to 1:")
count = 5
while count >= 1:
    print(f"  {count}")
    count = count - 1
print("  Blastoff! 🚀")

# # Example: User input simulation
# print("\nPassword attempt (up to 3 tries):")
# attempts = 0
# max_attempts = 3
# correct_password = "123456"

# # Simulating attempts
# simulated_passwords = ["wrong", "incorrect", "123456"]

# for password_attempt in simulated_passwords:
#     attempts += 1
#     if password_attempt == correct_password:
#         print(f"  Attempt {attempts}: '{password_attempt}' → CORRECT! ✓")
#         break
#     else:
#         print(f"  Attempt {attempts}: '{password_attempt}' → Wrong, try again")

# # --- LOOP Control (break and continue) ---
# print("\n8. Loop Control: BREAK and CONTINUE")
# print("-" * 50)

# print("BREAK - Exit loop when condition is met:")
# for i in range(1, 10):
#     if i == 5:
#         print(f"  Found 5! Stopping here.")
#         break
#     print(f"  {i}")

# print("\nCONTINUE - Skip to next iteration:")
# print("Counting 1-5 but skipping 3:")
# for i in range(1, 6):
#     if i == 3:
#         continue  # Skip this iteration
#     print(f"  {i}")

# print("\n" + "=" * 70)
# print("PART 3: ARRAYS (LISTS in Python)")
# print("=" * 70)

# # --- Creating Lists ---
# print("\n9. Creating Lists (arrays)")
# print("-" * 50)

# # List of numbers
# numbers = [10, 20, 30, 40, 50]
# print(f"Numbers: {numbers}")

# # List of strings
# students = ["Alice", "Bob", "Charlie", "Diana"]
# print(f"Students: {students}")

# # Mixed list
# mixed = [1, "hello", 3.14, True]
# print(f"Mixed list: {mixed}")

# # Empty list
# empty = []
# print(f"Empty list: {empty}")

# # --- Accessing Elements ---
# print("\n10. Accessing Elements by Index")
# print("-" * 50)

# grades = [85, 90, 78, 95, 88]
# print(f"Grades: {grades}")

# print(f"First grade (index 0): {grades[0]}")
# print(f"Third grade (index 2): {grades[2]}")
# print(f"Last grade (index -1): {grades[-1]}")
# print(f"Second to last (index -2): {grades[-2]}")

# # --- List Length ---
# print("\n11. Getting List Length")
# print("-" * 50)

# colors = ["red", "green", "blue", "yellow"]
# print(f"Colors: {colors}")
# print(f"Number of colors: {len(colors)}")

# # --- Adding Elements ---
# print("\n12. Adding Elements to a List")
# print("-" * 50)

# shopping_list = ["milk", "eggs", "bread"]
# print(f"Original list: {shopping_list}")

# shopping_list.append("cheese")  # Add at end
# print(f"After append('cheese'): {shopping_list}")

# shopping_list.insert(1, "butter")  # Add at specific position
# print(f"After insert(1, 'butter'): {shopping_list}")

# # --- Removing Elements ---
# print("\n13. Removing Elements from a List")
# print("-" * 50)

# items = ["pen", "pencil", "eraser", "ruler"]
# print(f"Original list: {items}")

# items.remove("eraser")  # Remove by value
# print(f"After remove('eraser'): {items}")

# removed_item = items.pop(0)  # Remove by index
# print(f"After pop(0): {items} (removed: '{removed_item}')")

# # --- List Slicing ---
# print("\n14. List Slicing (getting sub-lists)")
# print("-" * 50)

# letters = ["a", "b", "c", "d", "e", "f"]
# print(f"Letters: {letters}")

# print(f"letters[1:4]: {letters[1:4]}")  # from index 1 to 3
# print(f"letters[0:3]: {letters[0:3]}")  # first 3 elements
# print(f"letters[2:]: {letters[2:]}")   # from index 2 to end
# print(f"letters[:3]: {letters[:3]}")   # from start to index 2

# # --- Looping Through Lists ---
# print("\n15. Common List Operations with Loops")
# print("-" * 50)

# scores = [45, 67, 89, 56, 90]
# print(f"Scores: {scores}")

# # Find sum
# total = 0
# for score in scores:
#     total = total + score
# print(f"Sum of scores: {total}")

# # Find average
# average = total / len(scores)
# print(f"Average score: {average:.2f}")

# # Find maximum
# max_score = scores[0]
# for score in scores:
#     if score > max_score:
#         max_score = score
# print(f"Highest score: {max_score}")

# # --- Sorting ---
# print("\n16. Sorting Lists")
# print("-" * 50)

# unsorted = [5, 2, 8, 1, 9, 3]
# print(f"Original: {unsorted}")

# unsorted.sort()  # Sort in ascending order
# print(f"After sort(): {unsorted}")

# names = ["Zara", "Alice", "Bob", "Charlie"]
# names.sort()
# print(f"Names sorted: {names}")

# # --- Searching in List ---
# print("\n17. Searching in a List")
# print("-" * 50)

# fruits = ["apple", "banana", "orange", "grape"]

# if "banana" in fruits:
#     print("Banana is in the list!")
#     position = fruits.index("banana")
#     print(f"Banana is at index: {position}")

# if "mango" in fruits:
#     print("Mango is in the list!")
# else:
#     print("Mango is NOT in the list!")

# print("\n" + "=" * 70)
# print("PRACTICAL EXAMPLE: COMBINING EVERYTHING")
# print("=" * 70)

# print("\nStudent Grade Management System:")
# print("-" * 50)

# # List of student scores
# student_scores = [75, 82, 65, 90, 78, 88, 72]

# # Variables for statistics
# passing_count = 0
# failing_count = 0

# print(f"Student scores: {student_scores}")
# print(f"Passing grade: 70\n")

# # Using loop to check each score
# for i, score in enumerate(student_scores):
#     student_num = i + 1
    
#     # Logic operations: determine status
#     if score >= 70 and score <= 100:
#         status = "PASS ✓"
#         passing_count += 1
#     elif score < 70 and score >= 0:
#         status = "FAIL ✗"
#         failing_count += 1
#     else:
#         status = "INVALID"
    
#     print(f"  Student {student_num}: {score} points → {status}")

# # Summary
# print(f"\nSummary:")
# print(f"  Total students: {len(student_scores)}")
# print(f"  Passed: {passing_count}")
# print(f"  Failed: {failing_count}")
# print(f"  Pass rate: {(passing_count / len(student_scores)) * 100:.1f}%")
