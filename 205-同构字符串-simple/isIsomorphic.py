def isIsomorphic(s: str, t: str) -> bool:
    if not s:
        return True
    dict = {}
    for i in range(len(s)):
        if s[i] in dict:
            if dict[s[i]] == t[i]:
                continue
            else:
                return False
        else:
            if dict and t[i] in dict.values():
                return False
            else:
                dict[s[i]] = t[i]
    return True


def main():
    s = 'egg'
    t = 'add'
    print(isIsomorphic(s, t))


if __name__ == '__main__':
    main()