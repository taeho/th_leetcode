from typing import List

# https://leetcode.com/problems/product-of-array-except-self/
# Given an array nums of n integers where n > 1,  return an array output such
# that output[i] is equal to the product of all the elements of nums except nums[i].
#
# Example:
#
# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# Constraint: It's guaranteed that the product of the elements of any prefix
# or suffix of the array (including the whole array) fits in a 32 bit integer.
#
# Note: Please solve it without division and in O(n).

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        p = 1
        # 왼쪽 곱셈
        for i in range(len(nums)):
            output.append(p)
            p = p * nums[i]

        p = 1
        # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
        for i in range(len(nums)-1, 0 -1, -1): # nums를 거꾸로 탐색
            output[i] = output[i] * p # 메모리 공간 절약을 위해 output에 바로 곱해서 값을 저장
            p = p * nums[i]

        return output

if __name__ == '__main__':
    s1 = Solution()
    input1 = [1,2,3,4]
    print(s1.productExceptSelf(input1))