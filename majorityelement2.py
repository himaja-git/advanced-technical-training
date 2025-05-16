class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = {}
        n = len(nums)
        
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        result = []
        for key, value in d.items():
            if value > n // 3:
                result.append(key)
        
        return result
