class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # collect profits to a listand initial profit is 0
        profits = [0]
        # make last day price as current high price
        current_high = prices[-1]
        # iterate over second last to first element
        # if current price is greater than current high price update current high price
        # else calculate the profit and store it to the profits list
        # return the maximum of the profits
        for i in range(len(prices) - 2, -1, -1):
            if prices[i] > current_high:
                current_high = prices[i] 
            else:
                profit = current_high - prices[i]
                profits.append(profit)
        return max(profits)
        