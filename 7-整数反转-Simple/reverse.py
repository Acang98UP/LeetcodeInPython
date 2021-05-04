def reverse(x: int) -> int:
    if x <= 0:
        flag = -1
    else:
        flag = 1
    x = abs(x)
    string = list(str(x))
    string = string[::-1]
    new_int = int(''.join(string)) * flag
    if flag >= 2 ** 31 - 1 or flag <= -1 * 2 ** 31:
        return 0
    return new_int


def main():
    x = -123
    print(reverse(x))


if __name__ == '__main__':
    main()