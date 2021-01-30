def isValid(s: str) -> bool:
    dic = {'(': ')', '[': ']', '{': '}', '?': '?'}
    stack = ['?']
    for c in s:
        if c in dic:
            stack.append(c)
        elif dic[stack.pop()] != c:
            return False
        return len(stack) == 1



def main():
    s = '()[]{}'
    print(isValid(s))


if __name__ == '__main__':
    main()