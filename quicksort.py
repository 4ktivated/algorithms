def quicksort(nums: list):
    if len(nums) <= 1:
        return nums
    head = []
    midl = []
    tail = []
    opin = nums[-1]
    for i in nums:
        if i < opin:
            head.append(i)
        elif i == opin:
            midl.append(i)
        elif i > opin:
            tail.append(i)
    return quicksort(head) + midl + quicksort(tail) 


nums = [22, 5, 1, 18, 99, 56, 234, 164, 3146, 21, 4]

print(quicksort(nums))