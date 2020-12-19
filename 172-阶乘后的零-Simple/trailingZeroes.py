def trailingZeroes(n: int) -> int:
    count = 0
    while n > 0:
        count += int(n / 5)
        n = n / 5
    return count

# 寻找数字规律

def main():
    n = 6
    print(trailingZeroes(n))

if __name__ == '__main__':
    main()