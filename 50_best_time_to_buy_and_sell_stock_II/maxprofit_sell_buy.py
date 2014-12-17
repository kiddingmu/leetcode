class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        profit = 0
        if not prices:
            return 0
        else:
            cur_price = prices[0]
        for i in xrange(1, len(prices)):
            if prices[i] > cur_price:
                profit += (prices[i] - cur_price)
            cur_price = prices[i]

        return profit

if __name__ == "__main__":
    solution = Solution()
    #prices = [1,10,2,1,4,3,8,6]
    prices = [10, 1]
    print solution.maxProfit(prices)
