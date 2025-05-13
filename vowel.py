vowels = {'a', 'e', 'i', 'o', 'u'}

user_input = input("Enter a string: ")

count = sum(1 for char in user_input.lower() if char in vowels)

print(f"Number of vowels in the string: {count}")
