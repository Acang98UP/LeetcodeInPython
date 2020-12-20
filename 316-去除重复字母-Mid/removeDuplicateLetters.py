import collections


def removeDuplicateLetters(s: str) -> str:
    if len(s) == 0:
        return ''
    str_dict = collections.Counter(s)
    new_str = ''
    stack = []
    for i in s:
        if i not in stack:
            # 此处的判断条件是关键：首先栈中保存的是最后的结果
            # i < stack[-1]: 这个条件就是判断字典序的大小，为了避免误删，所以有了后面的条件
            # str_dict[stack[-1]] > 0:这个条件就是在保证后面还有的情况下，把小的安排在前面
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