def find_unique(list):
    return [x for x in list if list.count(x) == 1]

user_input = input('Enter a list of numbers: ')

data = list(map(int, user_input.split()))

unique_values = find_unique(data)
print("Unique values:", unique_values)

