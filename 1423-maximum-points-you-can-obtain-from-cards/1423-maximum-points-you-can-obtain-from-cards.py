class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
      #tc O(n), sc -O(n)
        n=len(cardPoints)
        winsize=n-k
        winsum=sum(cardPoints[:winsize])
        mwinsum=winsum
        total=sum(cardPoints)
        for i in range(winsize,n):
            winsum+=cardPoints[i]-cardPoints[i-winsize]
            mwinsum=min(mwinsum,winsum)
        return total-mwinsum