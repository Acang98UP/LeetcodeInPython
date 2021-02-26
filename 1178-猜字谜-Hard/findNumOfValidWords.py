import collections
from typing import List


def findNumOfValidWords(words: List[str], puzzles: List[int]) -> List[int]:
    freq = collections.Counter()
    for word in words:
        mask = 0
        for c in word:
            mask |= 1 << (ord(c) - ord('a'))
        freq[mask] += 1
    res = []
    for puzzle in puzzles:
        total = 0
        for perm in subsets(puzzle[1:]):
            mask = 1 << (ord(puzzle[0]) - ord('a'))
            for c in perm:
                mask |= 1 << (ord(c) - ord('a'))
            total += freq[mask]
        res.append(total)
    return res


def subsets(words: List[int]) -> List[List[int]]:
    res = [""]
    for i in words:
        res = res + [i + word for word in res]
    return res


def main():
    words = ["aaaa", "asas", "able", "ability", "actt", "actor", "access"]
    puzzles = ["aboveyz", "abrodyz", "abslute", "absoryz", "actresz", "gaswxyz"]
    print(findNumOfValidWords(words, puzzles))


if __name__ == '__main__':
    main()