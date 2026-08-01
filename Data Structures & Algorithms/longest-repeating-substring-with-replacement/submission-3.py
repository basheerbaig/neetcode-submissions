class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l=r=0
        occurance = {}
        maxfreq =longest= 0

        for r,ch in enumerate(s):
            occurance[ch] = 1 + occurance.get(ch, 0)
            maxfreq = max(occurance[ch], maxfreq)
            if (r-l+1) - maxfreq > k:
                occurance[s[l]] -= 1
                l += 1
                
            longest = max(r-l+1, longest)
        return longest


             