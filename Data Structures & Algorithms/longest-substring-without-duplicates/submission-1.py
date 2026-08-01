class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        track = set()
        res = 0
        left = 0

        for right in range(len(s)):
            while s[right] in track:
                track.remove(s[left])
                left += 1
            track.add(s[right])
            res = max(res, right - left + 1)
        return res 
                   