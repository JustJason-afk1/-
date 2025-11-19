def sum_in_range(start, end):
    total = 0
    if start > end:
        start, end = end, start
    for num in range(start, end + 1):
        total += num
    return total

print(sum_in_range(1, 5))   # 15
print(sum_in_range(5, 1))   # 15