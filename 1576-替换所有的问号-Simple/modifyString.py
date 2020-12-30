def modifyString(s: str) -> str:
    s1 = 'abcdefghijklmnopqrstuvwxyz'
    result = list('0' + s + '0')
    i = 1
    while i < len(result) - 1:
        if result[i] == '?':
            j = 0
            while j < len(s1):
                if s1[j] not in [result[i - 1], result[i + 1]]:
                    result[i] = s1[j]
                    break
                j += 1
        i += 1
    return ''.join(result[1:-1])


def main():
    s = '?ab'
    print(modifyString(s))


if __name__ == '__main__':
    main()