#189.rotate array- leetcode problem
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k=k%n
        nums[:]=nums[-k:]+nums[:-k]

#another method using two pointers-
'''class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k=k%n
        def reve(s,e):
            while s<e:
                nums[s],nums[e]=nums[e],nums[s]
                s+=1
                e-=1
        reve(0,n-1)
        reve(0,k-1)
        reve(k,n-1)'''
