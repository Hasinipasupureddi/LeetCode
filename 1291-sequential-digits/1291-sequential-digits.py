class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = "123456789"
        result = []
        min_len = len(str(low))
        max_len = len(str(high))
        for length in range(min_len, max_len + 1):
            for start in range(10 - length):
                substring = digits[start : start + length]
                num = int(substring)
                if low <= num <= high:
                    result.append(num)
                    
        return result