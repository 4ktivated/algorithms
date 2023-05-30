
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
    head = arr[0]
    if len(arr) == 1:
        return arr[0]
    tail = maximum(arr[1:])
    if head > tail:
        return head
    else:
        return tail
    
    
arr = [22, 5, 1, 18, 99, 56, 234, 164, 3146, 21, 4]

print(maximum(arr))