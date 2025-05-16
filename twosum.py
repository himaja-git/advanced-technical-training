class Solution:
    def twoSum(self, nums: List[int], target: int):
        d={} #S.C-O(N)
        n=len(nums)
        for a in range(0,n): #T.C-O(N)
            b=target-nums[a]
            if(b in d):
                return [a,d[b]]
            else:
                d[nums[a]]=a
