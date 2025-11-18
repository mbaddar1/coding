"""
Problem Description
You are given a string s that contains opening parentheses '(', closing parentheses ')', and lowercase English letters.

Your task is to remove the minimum number of parentheses (either '(' or ')') from any positions in the string to make the remaining parentheses valid. Return any valid string after the removal.

A valid parentheses string follows these rules:

It can be an empty string or contain only lowercase letters
It can be formed by concatenating two valid strings A and B (written as AB)
It can be written as (A) where A is a valid string (meaning every opening parenthesis has a matching closing parenthesis in the correct order)
For example:

"lee(t(c)o)de" is valid (all parentheses are balanced)
"a)b(c)d" is invalid (the first ) has no matching ()
"))(( is invalid (parentheses are not in the correct order)

https://algo.monster/liteproblems/1249
https://github.com/mbaddar1/leetcode-company-wise-problems/blob/main/Meta/1.%20Thirty%20Days.csv#L2
"""
from typing import Any


class MyStack:
    def __init__(self):
        self.arr = []
    def push(self, x:Any):
        self.arr.append(x)
    def pop(self):
        return self.arr.pop()
    def is_empty(self) -> bool:
        return len(self.arr) == 0
def fix_str(s: str) -> str:
    par_stack = MyStack()
    n = len(s)
    # pass 1 : get wrong parentheses indices
    bad_indices = set()
    for i in range(n):
        if s[i]=='(':
            par_stack.push((s[i],i))
        elif s[i]==')':
            if not par_stack.is_empty():
                par_stack.pop()
            else:
                bad_indices.add(i)
    # get bad indices

    while not par_stack.is_empty():
        c =par_stack.pop()
        bad_indices.add(c[1])
    new_s = ""
    for i in range(n):
        if i not in bad_indices:
            new_s += s[i]
    return new_s

    # pass 2 : get wrong
if __name__ == '__main__':
    # s = "lee(t(c)o)de"
    # r = fix_str(s)
    #
    s = "a)b(c)d"
    r = fix_str(s)
    print(r)
    #
    s = "))(("
    r = fix_str(s)
    print(r)

