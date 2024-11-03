#each index represents a day and on each index the price is stored. 
#Example: [5, 7, 2] means Day 0 it's 5, Day 1 is 7) 
#and returns the maximum profit you can achieve by buying and selling on different days
def max_profit(prices):
   

    profits = [0]*len(prices) # Initialize the list of profits

    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profits[i] = prices[i] - prices[i - 1]

    # Calculating the maximum profit from the profits list
    max_profit = 0
    for profit in profits:
        max_profit += profit

    return max_profit
prices=[5,7,2,5,8]
result=max_profit(prices)
print(result)










#[5,7,2]
#for day 1 -> price=5
#for day 2 -> price=7  profit=7-5=2
#for day 3 ->price=2   profit=2-7 not profit