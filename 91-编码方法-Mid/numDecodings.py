def numDecodings(s: str) -> int:
    if s[0] == '0':
        return 0
    if len(s) == 1:
        return 1

    legalstr = set(str(i) for i in range(1, 27))

    dp = [0] * (len(s) + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(1, len(s)):
        if s[i] not in legalstr:
            if s[i - 1: i + 1] not in legalstr:
                return 0
            else:
                dp[i + 1] = dp[i - 2 + 1]  # 因为dp多了一个，所以集体加1
        else:
            if s[i - 1: i + 1] in legalstr:
                dp[i + 1] = dp[i - 1 + 1] + dp[i - 2 + 1]
            else:
                dp[i + 1] = dp[i - 1 + 1]
    return dp[-1]


def main():
    s = '12'
    print(numDecodings(s))


if __name__ == '__main__':
    main()