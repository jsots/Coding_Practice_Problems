class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_day, sell_day = 0, 1
        max_profit = 0
        while sell_day < len(prices):
            if prices[buy_day] < prices[sell_day]:
                profit = prices[sell_day] - prices[buy_day]
                max_profit = max(max_profit, profit)
            else:
                buy_day = sell_day
            sell_day += 1
        
        return max_profit


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # keep track of max profit as a variable
        # buy day is one variable
        # sell day is another variable
        # if buy day less than sell day, compare to current max profit and keep highest value
        # then, move only the sell day to get highest profit
        # if the sell day is less than buy day, then that becomes the new buy day
        # return max profit
        # Questions:
        # What if there are two opportunities to yield a max profit?
        buy_day = 0
        sell_day = 1
        max_profit = 0

        while sell_day < len(prices):
            buy = prices[buy_day]
            sell = prices[sell_day]

            if buy > sell:
                buy_day = sell_day
                sell_day += 1
            else:
                max_profit = max(max_profit, sell - buy)
                sell_day += 1
        
        return max_profit


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy_day = 0
        sell_day = 1
        max_profit = 0

        while sell_day < len(prices):
            buy = prices[buy_day]
            sell = prices[sell_day]

            if buy > sell:
                buy_day = sell_day
            else:
                max_profit = max(max_profit, sell - buy)
            sell_day += 1
        
        return max_profit



