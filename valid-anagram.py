class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic1, dic2 = {}, {}
        for c in s:
            dic1[c] = dic1.get(c,0) + 1
        for c in t:
            dic2[c] = dic2.get(c,0) + 1
        return dic1 == dic2

    def isAnagram2(self, s, t):
        list1, list2 = [0]*26, [0]*26
        for c in s:
            list1[ord(c)-ord('a')] +=1
        for c in t:
            list2[ord(c)-ord('a')] +=1
        return list1 == list2

    def isAnagram3(self, s, t):
        return sorted(s) == sorted(t)

if __name__ == "__main__" :
    s = Solution()
    print(s.isAnagram("ABB","BBA"))
    print(s.isAnagram2("abb","bba"))
    print(s.isAnagram3("bba","abb"))
