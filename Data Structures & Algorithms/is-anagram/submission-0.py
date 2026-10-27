class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap = {}
        tmap = {}
        for c in s:
            if smap.get(c) == None:
                smap[c] = 1
            elif smap.get(c) != None:
                smap[c]+=1
        
        for d in t:
            if tmap.get(d) == None:
                tmap[d]=1
            elif tmap.get(d) != None:
                tmap[d]+=1
        
        if smap==tmap:
            return True
        else:
            return False