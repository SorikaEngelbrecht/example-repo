def largest_num(list):
    n = len(list)
    if n == 1:
        return list[0]
    if list[n-1] > list[n-2]:
        list[n-2] = list[n-1]
    return largest_num(list[:n-1])


num_list = [1, 4, 5, 3]
print(f"{largest_num(num_list)}")
