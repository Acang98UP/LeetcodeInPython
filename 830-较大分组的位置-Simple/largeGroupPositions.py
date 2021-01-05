from typing import List


def largeGroupPositions(s: str) -> List[List[int]]:
    if len(s) == 0:
        return []
    res = []
    stack = []
    begin, end = 0, 0
    for i in range(len(s)):
        if s[begin] == s[i]:
            end = i
            if (end - begin + 1) >= 3:
                stack.append(end)
                if i == len(s) - 1:
                    res.append([begin, stack[-1]])
                    stack.clear()
        else:
            while stack:
                res.append([begin, stack[-1]])
                stack.clear()
            begin = end = i
    return res


def main():
    s = 'abcdddeeeeaabbbcd'
    print(largeGroupPositions(s))


if __name__ == '__main__':
    main()