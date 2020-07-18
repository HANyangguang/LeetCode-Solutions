'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:
All given inputs are in lowercase letters a-z.
'''


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        for s in strs:
            if s == '':
                return ''
        c = strs[0][0]
        for s in strs[1:]:
            if s[0] != c:
                return ''
        strs = [s[1:] for s in strs]
        return s[0] + self.longestCommonPrefix(strs)