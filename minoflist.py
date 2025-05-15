def find_min_recursive(lst):
    if len(lst) == 1:
        return lst[0]
    return min(lst[0], find_min_recursive(lst[1:]))

user_input = input("Enter numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))
print("Minimum value:", find_min_recursive(numbers))
