class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        length = 0
        sets = set()
        i = 0

        for j in range(len(s)):
            while s[j] in sets:
                sets.remove(s[i])
                i += 1
            sets.add(s[j])
            length = max(length, j - i + 1)

        return length        