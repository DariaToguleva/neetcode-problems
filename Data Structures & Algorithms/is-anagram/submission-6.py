class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapS = {}
        mapT = {}

        for numS in s:
            mapS[numS] = mapS.get(numS, 0) + 1

        for numT in t:
            mapT[numT] = mapT.get(numT, 0) + 1

        if mapS == mapT:
            return True
        return False        