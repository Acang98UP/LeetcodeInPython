from typing import List


def candy(ratings: List[int]) -> int:
    if (n := len(ratings)) == 0:
        return 0
    left = [1] * n
    right = left[:]
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            left[i] = left[i - 1] + 1
    count = left[-1]
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            right[i] = right[i + 1] + 1
        count += max(left[i], right[i])
    return count


def main():
    ratings = [1, 3, 4, 5, 2]
    print(candy(ratings))

if __name__ == '__main__':
    main()