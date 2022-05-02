class Solution:
    def getPrefix(self, str1, str2):
        result = ""
        for i in range(min(len(str1), len(str2))):
            if str1[i] == str2[i]:
                result += str1[i]
                continue
            break
        return result

    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        if len(strs) < 2:
            return strs[0]
        for i in range(len(strs)):
            if i == 0:
                prefix = self.getPrefix(strs[i], strs[i+1])
            elif i == 1:
                continue
            else:
                prefix = self.getPrefix(strs[i], prefix)
            print(prefix)
        return prefix
