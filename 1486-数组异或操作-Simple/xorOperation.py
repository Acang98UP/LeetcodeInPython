def xorOperation(n: int, start: int) -> int:
    def sumXor(x):
        if x % 4 == 0:
            return x
        if x % 4 == 1:
            return 1
        if x % 4 == 3:
            return 0
        return x + 1

    e = n & start & 1
    s = start >> 1
    ans = sumXor(s - 1) ^ sumXor(s + n - 1)
    return ans << 1 | e


def main():
    n = 5
    start = 0
    print(xorOperation(n, start))


if __name__ == '__main__':
    main()