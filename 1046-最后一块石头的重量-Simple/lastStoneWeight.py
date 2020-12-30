from typing import List


def lastStoneWeight(stones: List[int]) -> int:
    while len(stones) != 0 and len(stones) != 1:
        stones = sorted(stones)
        bigger, smaller = stones[-1], stones[-2]
        if bigger == smaller:
            stones.pop()
            stones.pop()
        else:
            stones.pop()
            stones.pop()
            stones.append(bigger - smaller)
    if len(stones) == 0:
        return 0
    if len(stones) == 1:
        return stones[0]


def main():
    stones = [2, 7, 4, 1, 8, 1]
    print(lastStoneWeight(stones))


if __name__ == '__main__':
    main()