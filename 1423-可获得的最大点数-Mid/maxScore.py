from typing import List


def maxScore(cardPoints: List[int], k: int) -> int:
    sums = [0]
    for i in cardPoints:
        sums.append(sums[-1] + i)
    print(sums)
    n = len(cardPoints)
    res = 0
    for i in range(k + 1):
        # 用总数减去其他的元素，就剩余区间中的元素之和
        res = max(res, sums[-1] - (sums[i + (n - k)] - sums[i]))
    return res


def main():
    cardPoints = [1, 2, 3, 4, 5, 6, 1]
    k = 3
    print(maxScore(cardPoints, k))


if __name__ == '__main__':
    main()