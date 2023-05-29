def arr_sum(arr: list):
    if arr == []:
        return 0
    head = arr.pop()
    return head + arr_sum(arr)



def lenght_arr(arr: list):
    if arr == []:
        return 0
    return 1 + lenght_arr(arr[1:])


def maximum(arr: list):
    
    return 


arr = list(range(100))
print(lenght_arr(arr))
print(arr_sum(arr))

