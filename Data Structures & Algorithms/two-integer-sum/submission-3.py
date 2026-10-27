class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        s = {}
        for i in range(len(nums)):
            if s.get(target-nums[i]) != None:
                return [s.get(target-nums[i]), i]
            else:
                s[nums[i]] = i