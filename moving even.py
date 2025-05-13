lst = list(map(int, input("Enter numbers: ").split()))
odds = [x for x in lst if x % 2 != 0]
evens = [x for x in lst if x % 2 == 0]
result = odds + evens
print("Reordered list:", result)
