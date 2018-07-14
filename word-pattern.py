class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        list = str.split()
        dic = {}
        for c, s in pattern, list:
            if c in dic:
                if dic[c] != s:
                    return False
            else:
                dic[c] = s

if __name__ == "__main__" :
    s = Solution()
    print(s.wordPattern("abba", "dog cat cat dog"))
