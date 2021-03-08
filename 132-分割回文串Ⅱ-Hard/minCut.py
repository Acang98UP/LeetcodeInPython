def minCut(s: str) -> int:
    N = len(s)
    dp = [N] * N
    for i in range(N):
        if isPalindrome(s[0: i + 1]):
            dp[i] = 0
            continue
        for j in range(i):
            if isPalindrome(s[j + 1: i + 1]):
                dp[i] = min(dp[i], dp[j] + 1)
    return dp[N - 1]


def isPalindrome(s: str):
    return s == s[::-1]


def main():
    s = 'aab'
    print(minCut(s))


if __name__ == '__main__':
    main()