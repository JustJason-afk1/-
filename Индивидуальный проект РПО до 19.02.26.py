def find_max(lst):
    if len(lst) == 1:
        return lst[0]

    max_rest = find_max(lst[1:])

    if lst[0] > max_rest:
        return lst[0]
    else:
        return max_rest
def split_number(n, current=[]):
    if n == 0:
        print(current)
        return

    for i in range(1, n + 1):
        split_number(n - i, current + [i])
print(find_max([3, 7, 2, 9, 5]))
split_number(4)
