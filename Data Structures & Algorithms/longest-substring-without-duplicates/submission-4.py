class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subset = set()
        l = r = longest = 0

        for ch in s:
            # shrink the window until 'ch' is no longer duplicated
            while ch in subset:
                subset.remove(s[l])
                l += 1

            subset.add(ch)
            # r currently points at 'ch'
            longest = max(longest, r - l + 1)
            r += 1

        return longest
