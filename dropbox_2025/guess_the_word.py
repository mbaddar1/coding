"""
https://leetcode.com/problems/guess-the-word/?envType=company&envId=dropbox&favoriteSlug=dropbox-six-months
first attempt
10 out of 13
https://leetcode.com/problems/guess-the-word/submissions/1857580879
good link
https://algo.monster/liteproblems/843
"""
from typing import List, Tuple

class Solution:
    WORD_LEN = 6
    MAX_TRY = 30
    def findSecretWord(self, words: List[str], master: 'Master') -> None:

        for i in range(Solution.MAX_TRY):
            word = words.pop(0)
            r = master.guess(word)
            if r==Solution.WORD_LEN:
                break
            elif r>=0:
                for j in range(1,len(words)):

                    if j < len(words) and Solution.__match_two_words(word,words[j])!=r:
                        del words[j]


    @staticmethod
    def __match_two_words(word1:str, word2:str):
        assert len(word1) == len(word2)
        cnt = 0
        for i in range(len(word1)):
            if word1[i] == word2[i]:
                cnt+=1
        return cnt