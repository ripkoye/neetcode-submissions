class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        longest = 0
        for n in nums:
            s.add(n)
        for n in nums:
            count=1
            if n-1 not in s:
                i=1
                while n+i in s:
                    count+=1
                    i+=1
            longest = max(count, longest)
                    
        return longest
