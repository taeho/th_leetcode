from typing import List

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