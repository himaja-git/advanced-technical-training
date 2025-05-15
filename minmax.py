def find_min_max(lst):
    if len(lst) == 1:
        return lst[0], lst[0]
    mid = len(lst) // 2
    left, right = lst[:mid], lst[mid:]
    min1, max1 = find_min_max(left)
    min2, max2 = find_min_max(right)
    return (min1 if min1 < min2 else min2, max1 if max1 > max2 else max2)

s = input("Enter numbers separated by spaces: ")
nums = []
num = ''
for ch in s + ' ':
    if ch != ' ':
        num += ch
    else:
        if num:
            nums.append(int(num))
            num = ''
minimum, maximum = find_min_max(nums)
print("Minimum:", minimum)
print("Maximum:", maximum)
