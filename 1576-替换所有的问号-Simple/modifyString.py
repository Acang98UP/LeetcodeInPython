def modifyString(s: str) -> str:
    if s == '':
        return ''
    if len(s) == 1:
        if s == '?':
            return 'a'
    left, point, right = 0, 1, 2
    if right > len(s) - 1:
        right = point
    while point < len(s):
        if s[point] == '?':
            pass


def main():
    s = '?ab'
    print(modifyString(s))


if __name__ == '__main__':
    main()