#2785.Sorted vowels in a string- leetcode
class Solution:
    def sortVowels(self, s: str) -> str:
        arr=set('AEIOUaeiou')
        result=[]
        for ch in s:
            if ch in arr:
                result.append(ch)
        result.sort()
        p=0
        ans=[]
        for ch in s:
            if ch in arr:
                ans.append(result[p])
                p+=1
            else:
                ans.append(ch)
        return ''.join(ans)
