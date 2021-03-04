from typing import List


def maxEnvelopes(envelopes: List[List[int]]) -> int:
    if not envelopes:
        return 0
    N = len(envelopes)
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    res = 0
    dp = [1] * N
    for i in range(N):
        for j in range(i):
            if envelopes[j][1] < envelopes[i][1]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


def main():
    # envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
    envelopes = [[2, 100], [3, 200], [4, 300], [5, 500], [5, 400], [5, 250], [6, 370], [6, 360], [7, 380]]
    print(maxEnvelopes(envelopes))


if __name__ == '__main__':
    main()