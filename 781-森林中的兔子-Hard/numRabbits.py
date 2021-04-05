import collections
from typing import List


def numRabbits(answers: List[int]) -> int:
    count = collections.Counter(answers)
    return sum((count[x] + x) // (x + 1) * (x + 1) for x in count)


def main():
    answers = [1, 1, 2]
    print(numRabbits(answers))


if __name__ == '__main__':
    main()