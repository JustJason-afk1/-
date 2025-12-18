#нахождение наибольшего элемента в списке
def max_element(lst):
    if len(lst) == 1:
        return lst[0]
    m = max_element(lst[1:])
    if lst[0] > m:
        return lst[0]
    else:
        return lst[1] 
#рекурсивное разбирание чисел
def split_number(n, current=[], start=1):
    if n == 0:
        print(current)
        return
    for i in range(start, n):   
        split_number(n - i, current + [i], i)
