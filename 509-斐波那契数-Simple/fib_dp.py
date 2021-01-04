def fib(n: int) -> int:
    # 便捷的解决方案：动态规划
    dp_0, dp_1 = 0, 1
    for _ in range(n):
        dp_0, dp_1 = dp_1, dp_1 + dp_0
    return dp_0


def main():
    n = 4
    print(fib(n))


if __name__ == '__main__':
    main()