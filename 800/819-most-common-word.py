# 819. Most Common Word
# https://leetcode.com/problems/most-common-word/
# Given a string paragraph and a string array of the banned words banned,
# return the most frequent word that is not banned.
# It is guaranteed there is at least one word that is not banned, and that the answer is unique.
#
# The words in paragraph are case-insensitive and the answer should be returned in lowercase.
# Example 1:
# Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
# Output: "ball"
# Explanation:
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does),
#     so it is the most frequent non-banned word in the paragraph.
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"),
# and that "hit" isn't the answer even though it occurs more because it is banned.

import collections
import re
from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # 아래 정규식은 단어 문자(\w)가 아닌 모든 문자를 공백(' ')으로 치환Substitute하는 역할
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
            .lower().split()
                 if word not in banned]

        counts = collections.Counter(words)
        # 가장 흔하게 등장하는 단어의 첫 번째 인덱스 리턴
        return counts.most_common(1)[0][0]

if __name__ == '__main__':
    p1 = Solution()
    input1 = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]

    print("input=")
    print(input1)
    print("output=")
    print(p1.mostCommonWord(input1, banned))
