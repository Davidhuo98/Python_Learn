def has_duplicates(lst):
    return len(lst) != len(set(lst))
lst = [1, 2, 3, 4, 5, 3]
print(has_duplicates(lst))
# 输出：True