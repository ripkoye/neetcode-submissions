class Solution:
    from collections import defaultdict
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hashmap = defaultdict(int)
        for i in nums:
            hashmap[i]+=1
        l = sorted(list(hashmap.items()))
        buckets = [[] for _ in range(len(nums)+1)]
        for key, value in hashmap.items():
            buckets[value].append(key)
        ans = []
        for i in range(len(buckets)):
            if buckets[len(buckets)-1-i] != []:
                ans.extend(buckets[len(buckets)-1-i])
                k-=len(buckets[len(buckets)-1-i])
            if k==0:
                break
        return ans