from typing import List


def minDays(bloomDay: List[int], m: int, k: int) -> int:
    if k * m > len(bloomDay):
        return -1

    def canMake(days: int) -> bool:
        bouquets = flowers = 0
        for i, bloom in enumerate(bloomDay):
            if bloomDay[i] <= days:
                flowers += 1
                if flowers == k:
                    bouquets += 1
                    if bouquets == m:
                        break
                    flowers = 0
            else:
                flowers = 0
        return bouquets == m

    low, high = 1, max(bloomDay)
    while low < high:
        days = (low + high) // 2
        if canMake(days):
            high = days
        else:
            low = days + 1
    return low


def main():
    bloomDay = [1, 10, 3, 10, 2]
    m = 3
    k = 1
    print(minDays(bloomDay, m, k))


if __name__ == '__main__':
    main()