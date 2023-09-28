class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l = 0
        charset = set()
        res = 0

        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l += 1
            charset.add(s[r])
            res = max(res,r-l+1)
        return res
    
    


