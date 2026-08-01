class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l=0
        occurance = {}
        maxfreq =longest= 0

        for r,ch in enumerate(s):
            occurance[ch] = 1 + occurance.get(ch, 0)
            maxfreq = max(occurance[ch], maxfreq) #IMPORTANT LINE
            if (r-l+1) - maxfreq > k:
                occurance[s[l]] -= 1
                l += 1
                
            longest = max(r-l+1, longest)
        return longest


# Key idea
# In any window [l..r], if we want to make all chars the same, we only need to replace the ones that are not the most frequent char in that window.
# So replacements needed =

# (window\_size)−(maxfreq)
 
# If that number > k, window is invalid → shrink from left.