from typing import List
# https://leetcode.com/problems/valid-palindrome/
# Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
import collections
import re

from typing import Deque

class Solution:
    def isPalindrome3(self, s: str) -> bool:
        s = s.lower()

        # 정규식으로 불필요한 문자 필터링
        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]  # 슬라이싱

    # 데크 자료형 활용
    def isPalindrome(self, s: str) -> bool:
        # 자료형 데크로 선언
        strs: Deque = collections.deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False

        return True


    # 리스트변환방식
    def isPalindrome1(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum(): # 영문 숫자 판별
                strs.append(char.lower())

        # 팬린드롬 체크
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False

        return True

if __name__ == '__main__':
    p1 = Solution()
    # Input: s = "A man, a plan, a canal: Panama"
    # Output: true
    # Explanation: "amanaplanacanalpanama" is a palindrome.
    input1 = "A man, a plan, a canal: Panama"
    print(p1.isPalindrome2(input1))