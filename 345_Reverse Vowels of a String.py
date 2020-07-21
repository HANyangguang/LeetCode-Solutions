'''
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Input: "hello"
Output: "holle"

Example 2:
Input: "leetcode"
Output: "leotcede"

Note:
The vowels does not include the letter "y".
'''
class Solution:
    def reverseVowels(self, s: str) -> str:
        start = 0
        end = len(s) -1
        v = "aeiouAEIOU"
        s = list(s)
        while start<end:
            if s[start] in v and s[end] in v:
                t = s[start]
                s[start] = s[end]
                s[end] = t
                start += 1
                end -= 1  
            else:
                if s[start] not in v:
                    start += 1
                if s[end] not in v:
                    end -= 1 
        return ''.join(s)