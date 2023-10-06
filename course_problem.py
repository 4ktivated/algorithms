
# def shit(nums):
#     n = len(nums)
#     left = [1 for _ in range(n)]
#     for i in range(1, n):
#         left[i] = left[i-1] * nums[i -1]
#         temp = left[i]
#     right = [1 for _ in range(n)]
#     for i in range(n-2, -1, -1):
#         right[i] = right[i + 1] * nums[i + 1]
#         temp = right[i]
#     result = []
#     for i in range(n):
#         result.append(right[i] * left[i])
#     return result



# nums =[1,2,3,4]
# print(shit(nums))

nums = [0,0,1]
def moveZeroes(nums):
    n =len(nums)-1
    j = 0
    for i in range(n):
        if nums[j] == 0:
            nums.append(nums.pop(j))
        else:
            j += 1
    

moveZeroes(nums)
print(nums)