def removeDuplicates(S: str) -> str:
    if len(S) == 0 or len(S) == 1:
        return S
    stack = []
    for c in S:
        if stack and c == stack[-1]:
            stack.pop(-1)
            continue
        stack.append(c)
    return ''.join(stack)



def main():
    S = 'abbaca'
    print(removeDuplicates(S))


if __name__ == '__main__':
    main()