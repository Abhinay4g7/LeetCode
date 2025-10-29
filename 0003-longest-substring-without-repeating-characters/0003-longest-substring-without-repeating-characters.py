class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=0
        l=0
        r=0
        map =set()
        while l<len(s) and r<len(s):
            print("--",map)
            while s[r] in map and r<len(s) and l<len(s):
                map.remove(s[l])
                l+=1
            map.add(s[r])
            res=max(len(map),res)
            r+=1
        return res



        