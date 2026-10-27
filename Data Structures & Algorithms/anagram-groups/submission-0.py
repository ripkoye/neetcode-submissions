class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashmap = {}
        for s in strs:
            if hashmap.get(''.join(sorted(s))) == None:
                hashmap[''.join(sorted(s))] = [s]
            else:
                hashmap[''.join(sorted(s))].append(s)
        
        return list(hashmap.values())

            
        