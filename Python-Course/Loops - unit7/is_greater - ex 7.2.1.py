def is_greater(my_list, n):
    list = []
    for num in my_list:
        if num > n:
            list.append(num)
    return list

result = is_greater([1, 30, 25, 60, 27, 28], 28)
print(result)
