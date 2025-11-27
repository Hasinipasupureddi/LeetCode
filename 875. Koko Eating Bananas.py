#875. Koko Eating Bananas-leetcode
from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        while(low<=high):
            mid=(low+high)//2
            Sum=0
            for num in piles:
                Sum+=ceil(num/mid)
            if(Sum<=h):
                high=mid-1
            else:
                low=mid+1
        return low
