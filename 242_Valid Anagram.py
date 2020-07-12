'''
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_d = {}
        for i in s:
            if i in s_d:
                s_d[i] += 1
            else:
                s_d[i] = 1
        t_d = {}
        for i in t:
            if i in t_d:
                t_d[i] += 1
            else:
                t_d[i] = 1
        return s_d == t_d

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return(collections.Counter(s) == collections.Counter(t))
