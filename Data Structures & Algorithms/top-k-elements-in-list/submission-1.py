from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in hashmap.items():
            buckets[freq].append(num)

        ans = []
        for bucket in reversed(buckets):
            for num in bucket:
                ans.append(num)
                if len(ans) == k:
                    return ans