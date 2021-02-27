def longestSubstring(s: str, k: int) -> int:
    if len(s) < k:
        return 0
    for c in set(s):
        if s.count(c) < k:
            return max(longestSubstring(t, k) for t in s.split(c))
    return len(s)


def main():
    s = 'aaabb'
    k = 3
    print(longestSubstring(s, k))


if __name__ == '__main__':
    main()