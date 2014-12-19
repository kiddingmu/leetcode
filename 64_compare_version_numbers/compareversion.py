class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        ver1_array = version1.split('.')
        ver2_array = version2.split('.')
        len1 = len(ver1_array)
        len2 = len(ver2_array)
        minlen = min(len1, len2)
        for i in xrange(minlen):
            temp1 = int(ver1_array[i])
            temp2 = int(ver2_array[i])
            if temp1 == temp2:
                continue
            elif temp1 > temp2:
                return 1
            else:
                return -1
        else:
            if len1 == len2:
                return 0
            elif len1 > len2: 
                while minlen < len1:
                    if int(ver1_array[minlen]) == 0:
                        minlen += 1
                    else:
                        break
                else:
                    return 0
                return 1
            else:
                while minlen < len2:
                    if int(ver2_array[minlen]) == 0:
                        minlen += 1
                    else:
                        break
                else:
                    return 0
                return -1


if __name__ == "__main__":
    solution = Solution()
    ver1 = "1.0"
    ver2 = "1"
    print solution.compareVersion(ver1, ver2)
