#Exercise 1.2: List Manipulator

# Sum: 39
# Average: 4.875
# Max: 9, Min: 1
# Without duplicates: [5, 3, 8, 9, 1, 2]
# Sorted (asc): [1, 2, 3, 5, 8, 9]
# Even numbers: [8, 2]
# Odd numbers: [5, 3, 9, 1]

# Hints:
    # Use built-in functions: sum(), max(), min()
    # Use set() to remove duplicates
    # Use list comprehension for filtering

def list_manipulator():
    list_str = input("Enter a list of numbers separated by spaces: ")
    
    list_numbers = [int(num) for num in list_str.split()]
    print(f"Input list: {list_numbers}")
    total_sum = sum(list_numbers)
    average = total_sum / len(list_numbers)
    maximum = max(list_numbers)
    minimum = min(list_numbers)
    without_duplicates = list(set(list_numbers))
    sorted_list = sorted(list_numbers)
    even_numbers = [num for num in list_numbers if num % 2 == 0]
    odd_numbers = [num for num in list_numbers if num % 2 != 0]
    print(f"Sum: {total_sum}")
    print(f"Average: {average}")
    print(f"Max: {maximum}, Min: {minimum}")
    print(f"Without duplicates: {without_duplicates}")
    print(f"Sorted (asc): {sorted_list}")
    print(f"Even numbers: {even_numbers}")
    print(f"Odd numbers: {odd_numbers}")

list_manipulator()