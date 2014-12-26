class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        len1 = len(word1)
	len2 = len(word2)
	if len1 == 0:
            return len2
	if len2 == 0:
            return len1
	distance = {}
	for i in xrange(len1+1):
            distance[(i, 0)] = i
	for j in xrange(len2+1):
            distance[(0, j)] = j

	for i in xrange(1, len1+1):
            for j in xrange(1, len2+1):
                cur_distance = 0
		if word1[i-1] != word2[j-1]:
                    cur_distance = 1
            distance[(i,j)] = min(distance[(i-1,j)]+1, distance[(i,j-1)]+1, distance[(i-1,j-1)]+cur_distance)
        return distance[(len1,len2)]

if __name__ == "__main__":
    solution = Solution()
    word1 = "kitten"
    word2 = "sitting"
    print solution.minDistance(word1, word2)
