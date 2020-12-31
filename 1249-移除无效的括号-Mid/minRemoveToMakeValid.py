def minRemoveToMakeValid(s: str) -> str:
    if len(s) == 0:
        return ''
    stack = []
    for c in range(0, len(s)):
        if stack == [] and s[c] == ')':
            s.removeprefix()
        if s[c] == '(':
            stack.append(c)


def main():
    s = 'lee(t(c)o)de)'
    print(minRemoveToMakeValid(s))


if __name__ == '__main__':
    main()