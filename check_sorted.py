def chek_sorted(arr: list):
    for i in range(len(arr) - 1):
        if arr[i]>arr[i + 1]:
            return False
    return True


nums = [22, 5, 1, 18, 99, 56, 234, 164, 3146, 21, 4]
print(chek_sorted(nums))