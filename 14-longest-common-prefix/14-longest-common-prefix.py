class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        for i in zip(*strs):
            if i[:-1] == i[1:]:
                prefix += i[0]
            else:
                break
        return prefix
        