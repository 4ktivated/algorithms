#task_1
# n, s = [int(i) for i in input().split()]
# prices = [int(j) for j in input().split()]
# max_for_joe = 0
# for p in prices:  
#     if p > max_for_joe and p <= s:
#         max_for_joe = p
# print(max_for_joe)


#task_2
# s = 'fheriherffazfszkisrrs'
# letters_count = {}
# word = "sheriff"
# for letter in s:
#     if letter in letters_count:
#         letters_count[letter] += 1
#     else:
#         letters_count[letter] = 1
# max_words = float("inf")
# for letter in word:
#     if letter in letters_count:
#         if letters_count[letter] < max_words:
#             max_words = letters_count[letter]
#     else:
#         max_words = 0
#         break
# print (max_words)


#task3
def check_winning_sequence(n, sequence, winning_sequence):
    first_diff_index = -1
    last_diff_index = -1

    
    for i in range(n):
        if sequence[i] != winning_sequence[i]:
            if first_diff_index == -1:
                first_diff_index = i
            last_diff_index = i

   
    if first_diff_index == -1 or first_diff_index == last_diff_index:
        return "YES"
    elif (
        sequence[first_diff_index:last_diff_index+1] ==
        winning_sequence[first_diff_index:last_diff_index+1][::-1]
    ):
        return "YES"
    elif (
        sequence[first_diff_index:last_diff_index+1][::-1] ==
        winning_sequence[first_diff_index:last_diff_index+1]
    ):
        return "YES"

    return "NO"


n = 5
sequence =[1, 4, 2, 2, 4] #list(map(int, input().split()))
winning_sequence = [1, 4, 4, 2, 2] #list(map(int, input().split()))

result = check_winning_sequence(n, sequence, winning_sequence)
print(result)


#task4
# n, m = map(int, input().split())
# coins = list(map(int, input().split()))
# k = 0
# all_money = coins * 2
# sequence = []

# for i in all_money:
#     if n - i > 0:
#         n -= i
#         sequence.append(i)
#     if n - i < 0:
#         continue
#     if n - i == 0:
#         sequence.append(i)
#         print(len(sequence))
#         print(*sequence)
#         sequence = []
#         break
# if sequence is True:
#     print(-1)


