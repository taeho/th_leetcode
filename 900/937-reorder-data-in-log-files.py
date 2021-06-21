# 937. Reorder Data in Log Files
# You are given an array of logs. Each log is a space-delimited string of words,
#     where the first word is the identifier.
#
# There are two types of logs:
#      Letter-logs: All words (except the identifier) consist of lowercase English letters.
#      Digit-logs: All words (except the identifier) consist of digits.
#
# Reorder these logs so that:
#    1. The letter-logs come before all digit-logs.
#    2. The letter-logs are sorted lexicographically by their contents.
#        If their contents are the same, then sort them lexicographically by their identifiers.
#    3. The digit-logs maintain their relative ordering.
#    - 로그의 가장 앞부분은 식별자, 문자로 구성된 로그가 숫자보다 앞에 온다
#    - 식별자는 순서에 영향 안끼치고 대신 문자가 동일하면 식별자순으로
#    - 숫자 로그는 순서대로 한다.
#
# Return the final order of the logs.
# Example 1:
#   Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
#   Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
#   Explanation:
#      The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
#      The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".
#
# Constraints:
#
#     1 <= logs.length <= 100
#     3 <= logs[i].length <= 100
#     All the tokens of logs[i] are separated by a single space.
#     logs[i] is guaranteed to have an identifier and at least one word after the identifier.
#
#
#
#
from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        # 숫자로 변환가능한 로그는 digits에
        # 그렇지 않은 경우 문자 로그는 letters에 추가.
        letters, digits = [], []
        # 문자로 구성된 로그가 숫자 로그보다 이전에 오고,
        # 숫자로 로그는 입력순서대로 둔다.
        # 문자와 숫자를 구분하고 숫자는 나중에 그대로 이어 붙인다.
        # 로그자체는 숫자 로그도 모두 문자열로 지정되어 있으므로, 타입을 확인하면
        # 모두 문자로 출력된다. isdigit()함수를 이용해 숫자여부 판별
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        # 2개의 키를 람다 표현식으로 정렬
        # 식별자를 제외한 문자열 [1:]을 키로 하여 정렬,
        # 동일한 경우 후순위로 식별자[0]를 지정해 정렬하도록 
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        
        # 이어붙여서 리턴
        return letters + digits

if __name__ == '__main__':
    p1 = Solution()
    input1 = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    print("input=")
    print(input1)
    print("output=")
    print(p1.reorderLogFiles(input1))
