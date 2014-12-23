# Given an array of size n, find the majority element.
# The majority element is the element that appears more than [ n/2 ] times.
class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        """
        result = {}
        for item in num:
            result[item] = result.get(item, 0) + 1
        return result
        """
        stack = []
        for item in num:
            if not stack or stack[-1] == item:
                stack.append(item)
            else:
                stack.pop()
        return stack[0]

if __name__ == "__main__":
    solution = Solution()
    num = [1,2,5,4,5,6,5,5,5,5]
    print solution.majorityElement(num)
