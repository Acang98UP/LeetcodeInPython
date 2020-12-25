from typing import List


def findContentChildren(g: List[int], s: List[int]) -> int:
    count = 0
    g = sorted(g)
    s = sorted(s)
    i, j = 0, 0
    while i != len(g) and len(g) != 0 and len(s) != 0:
        if s[-1] < g[0]:
            return count
        while j != len(s) and len(g) != 0 and len(s) != 0:
            if s[j] >= g[i]:
                count += 1
                s.pop(j)
                g.pop(i)
                j = 0
                continue
            j += 1
        i += 1
    return count


def main():
    g = [1, 2, 3]
    s = [1, 1]
    print(findContentChildren(g, s))


if __name__ == '__main__':
    main()
