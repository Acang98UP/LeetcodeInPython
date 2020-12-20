import collections


def removeDuplicateLetters(s: str) -> str:
    if len(s) == 0:
        return ''
    str_dict = collections.Counter(s)
    new_str = ''
    stack = []
    for i in s:
        if i not in stack:
            while stack and i < stack[-1] and str_dict[stack[-1]] > 0:
                stack.pop()
            stack.append(i)
        str_dict[i] -= 1
    return new_str.join(stack)

def main():
    str = "cbacdcbc"
    print(removeDuplicateLetters(str))

if __name__ == '__main__':
    main()