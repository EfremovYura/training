"""
Given a string s, return the longest palindromic substring in s.



Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"


Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""
def longest_palindrome(s: str) -> str:
    start = 0
    max_len = 1
    len_s = len(s)
    for i in range(len_s-1):
        len_i = 1
        left = i - 1
        right = i + 1
        while left >= 0 and right < len_s and s[left] == s[right]:
            len_i += 2
            if len_i > max_len:
                start = left
                max_len = len_i
            left -= 1
            right += 1


        len_i = 0
        left = i
        right = i + 1
        while left >= 0 and right < len_s and s[left] == s[right]:
            len_i += 2
            if len_i > max_len:
                start = left
                max_len = len_i
            left -= 1
            right += 1
    return s[start: start + max_len]

if __name__ == "__main__":
    assert longest_palindrome('a') == 'a'
    assert longest_palindrome('aa') == 'aa'
    assert longest_palindrome('aaa') == 'aaa'
    assert longest_palindrome('aaaa') == 'aaaa'
    assert longest_palindrome('babad') == 'bab'
    assert longest_palindrome('cbbd') == 'bb'

    print("passed")