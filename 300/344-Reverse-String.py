# https://leetcode.com/problems/reverse-string/
# Write a function that reverses a string.
# The input string is given as an array of characters s.
#
# Example 1:
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
#
# Example 2:
# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
#
# Constraints
#    1 <= s.length <= 10^5
#    s[i] is a printable ascii character.

from typing import List

class Solution:
    # two pointer 를 이용한 방법: 2개의 포인터를 이용해 범위를 조정해가며 풀이
    def reverseString(self, s: List[str]) -> None:
        # left는 0부터 , right는 현재길이-1에서 시작
        left, right = 0, len(s) - 1

        # 왼쪽에서부터 증가, 오른쪽부터 감소하여 리턴없이 리스트내에서 조작
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        print(s)

    # 파이썬 방식, leetcode에서 accepted 되긴함
    def reverseString2(self, s: List[str]) -> None:
        s.reverse()
        print(s)

if __name__ == '__main__':
    p1 = Solution()
    input1 = ["h","e","l","l","o"]
    p1.reverseString(input1)


