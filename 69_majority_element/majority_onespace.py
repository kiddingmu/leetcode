# Given an array of size n, find the majority element.
# The majority element is the element that appears more than [ n/2 ] times.
class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        count = 1
        candidate = num[0]
        for item in num[1:]:
            if count == 0:
                candidate = item
                count = 1
            elif item == candidate:
                count += 1
            else:
                count -= 1
        return candidate


if __name__ == "__main__":
    solution = Solution()
    num = [1,2,5,4,5,6,5,5,5,5]
    print solution.majorityElement(num)
