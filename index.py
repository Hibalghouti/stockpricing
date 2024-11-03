#each index represents a day and on each index the price is stored. 
#Example: [5, 7, 2] means Day 0 it's 5, Day 1 is 7) 
#and returns the maximum profit you can achieve by buying and selling on different days
def max_profit(prices):
    if not prices:
        return 0  # if list of prices is empty

    profits = [0] * len(prices)  # Initialize the list of profits

    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profits[i] = prices[i] - prices[i - 1]

    # Calculating the maximum profit from the price list
    max_profit = 0
    for profit in profits:
        max_profit = max(max_profit, profit)  # Update max_profit

    return max_profit

# Example usage:
prices = [5,7,1,4,9,6]
print(max_profit(prices))  


#[5,7,1,4,9,6]
#for day 1 ->price=5
#for day 2 ->price=7  profit=7-5=2
#for day 3 ->price=1  profit=2-7 no profit
#for day=4 ->price=4  profit=4-1=3
#for day=5 ->price=9  profit=9-4=5
#for day=6 ->price=6  profit=6-9 no profit

#max profit=5