def equalSubstring(s: str, t: str, maxCost: int) -> int:
    N = len(s)
    costs = [0] * N
    for i in range(N):
        costs[i] = abs(ord(s[i]) - ord(t[i]))
    left, right = 0, 0
    res = 0
    sums = 0
    while right < N:
        sums += costs[right]
        while sums > maxCost:
            sums -= costs[left]
            left += 1
        res = max(res, right - left + 1)
        right += 1
    return res


def main():
    s = 'abcd'
    t = 'bcdf'
    cost = 3
    print(equalSubstring(s, t, cost))


if __name__ == '__main__':
    main()