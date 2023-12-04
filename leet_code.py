def maxProfit(prices) -> int:
    max_profit = 0
    current  = prices[0]
    for i in prices:
        current = min(current, i)
        max_profit = max(max_profit, i - current)
    return max_profit

example = [7,1,5,3,6,4]
print(maxProfit(example))