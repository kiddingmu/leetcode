class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        dic = {}
        for item in A:
            dic[item] = dic.get(item, 0) + 1
        #print dic
        interval = [0]*3
        for i in range(0, 3):
            if i == 0:
                interval[i] = dic.get(i, 0)
            else:
                interval[i] = dic.get(i, 0) + interval[i-1]

        for i in xrange(len(A)):
            if i < interval[0]:
                A[i] = 0
            elif i < interval[1]:
                A[i] = 1
            else:
                A[i] = 2

if __name__ == "__main__":
    A = [0, 1, 2, 1, 1, 2, 0]
    #A = [0]
    #A = [1]
    #A = []
    solution = Solution()
    solution.sortColors(A)
    print A
