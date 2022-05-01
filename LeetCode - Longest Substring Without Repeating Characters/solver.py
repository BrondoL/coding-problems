class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = list()
        substr = ""
        for x in s:
            if x not in substr:
                substr += x
            else:
                result.append(substr)
                i = substr.index(x)
                substr = substr[i+1:] + x
        result.append(substr)
        result = list(map(len, result))
        return max(result)
