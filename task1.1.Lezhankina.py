def parser(lst: list):
    size = len(lst)
    left = lst[:size // 2]
    right = lst[size // 2 + size % 2:]
    print('The first part:', left)
    print('The second part:', right)
    if sum(left) > sum(right):
        return True
    return False


lst = [26, 13, 6, 16, 17, 2, 0, 1]
print('Sum of the first part > the second part:', parser(lst))
