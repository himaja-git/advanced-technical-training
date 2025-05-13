def convert_case(s):
    result = ''
    for char in s:
       
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)  
      
        elif 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)  
        else:
            result += char  
    return result


input_string = input("Enter a string: ")


output_string = convert_case(input_string)
print("Converted string:", output_string)

