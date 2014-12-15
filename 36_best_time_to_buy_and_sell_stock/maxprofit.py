class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        size = len(prices)
        if size < 2:
            return 0
        profits = [0] * size
        for i in xrange(1, size):
            profits[i] = max(profits[i], profits[i-1]+prices[i]-prices[i-1], prices[i]-prices[i-1])
        return max(profits)

if __name__ == "__main__":
    prices = [10,3,2,6,3,1]
    solution = Solution()
    print solution.maxProfit(prices)
