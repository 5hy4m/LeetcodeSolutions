class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i,value in enumerate(nums):
            if target - value in hashMap:
                return [hashMap[target - value],i]
            hashMap[value] = i
        return None