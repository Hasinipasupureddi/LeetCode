#leetcode problem number 78. subsets
class Solution:
    def subsets(self,nums:list[int])-> list[list[int]]:
        res=[]
        n=len(nums)
        for i in range(1<<n):      
            s=[]        
            for j in range(n):         
                if i&(1<<j):          
                    s.append(nums[j])
            res.append(s)
        return res
