"""
🟢 Problem: Longest Substring Without Repeating Characters
Problem Statement

Given a string s, find the length of the longest substring without repeating characters.

Examples

vbnet
Copy
Edit
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
vbnet
Copy
Edit
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
vbnet
Copy
Edit
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
Constraints

0 <= s.length <= 5 * 10^4

s consists of English letters, digits, symbols, and spaces.

✅ HINTS to get you started

Use a sliding window with two pointers.

Use a hash map to track the last index of each character.

Update the start of the window to skip over duplicates.
"""


def find_longest_substring(s):
    n = len(s)
    i = j = 0
    aux = dict()
    aux[s[i]] = i
    max_length = 1
    while j < n:
        idx = aux.get(s[j], None)
        if idx is None:
            aux[s[j]] = j
        else:
            if idx != j:
                i = idx + 1
        aux[s[j]] = j
        # while i < j and s[i] == s[j]:
        #     i += 1
        max_length = max(max_length, j - i + 1)

        j += 1
    return max_length


if __name__ == "__main__":
    r = find_longest_substring("abcabcbb")
    print(r)
    r = find_longest_substring("bbbbb")
    print(r)
    r = find_longest_substring("pwwkew")
    print(r)

