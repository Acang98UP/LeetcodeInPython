import functools


class Solution:
    @functools.lru_cache(None)
    def isScramble(self, s1: str, s2: str) -> bool:
        N = len(s1)
        if N == 0: return True
        if N == 1: return s1 == s2
        if sorted(s1) != sorted(s2):
            return False
        for i in range(1, N):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            elif self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                return True
        return False