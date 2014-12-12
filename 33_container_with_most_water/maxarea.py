class Solution:
    # @return an integer
    def maxArea(self, height):
        """
        size = len(height)
        max_area = [0] * size
        #return sum(height)
        for i in xrange(size):
            for j in xrange(i):
                area = min(height[i],height[j])*(i-j)
                if area > max_area[i]:
                    max_area[i] = area
        return max(max_area)
        """
        left = 0
        right = len(height)-1
        result = 0
        while left < right:
            result = max(result, (right-left)*min(height[left], height[right]))
            if height[left] < height[right]:
                left +=1
            else:
                right -=1
        return result

if __name__ == "__main__":
    solution = Solution()
    height = [2,4,8,4,5]
    print solution.maxArea(height)
