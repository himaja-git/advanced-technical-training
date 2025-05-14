n = int(input("Enter a number: "))
indexes = [i for i in range(n.bit_length()) if (n >> i) & 1]
print(indexes)
