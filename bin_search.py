def binary_search(my_list, num):
    low = 0
    hight = len(my_list) - 1
    cnt = 0
    while low <= hight:
        mid = int((low + hight) / 2)
        item = my_list[mid]
        if item == num:
            return mid
        elif item < num:
            low = mid + 1
        elif item > num:
            hight = mid - 1
        cnt += 1
        print(cnt)
    return None

my_list = list(range(100))
num = 73
print(binary_search(my_list, num))
