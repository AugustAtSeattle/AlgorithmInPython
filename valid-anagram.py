class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        dic = {}

        for c in s:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1

        for c in t:
            if c in dic:
                dic[c] -= 1
                if dic[c] == 0:
                    del dic[c]
            else:
                return False

        return True
