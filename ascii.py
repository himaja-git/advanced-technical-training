def sum_of_positions(input_string):
    total_sum = 0
    for char in input_string:
        if char.isalpha():  
           
            position = ord(char.lower()) - ord('a') + 1
            total_sum += position
    return total_sum


input_string = input("Enter a string: ")

result = sum_of_positions(input_string)
print(f"The sum of the positions of the alphabets in '{input_string}' is: {result}")
