#728.Self Dividing numbers-leetcode
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for num in range(left, right + 1):
            temp = num
            valid = True
            while temp > 0:
                digit = temp % 10
                if digit == 0 or num % digit != 0:
                    valid = False
                    break
                temp //= 10
            if valid:
                result.append(num)
        return result
        
