from typing import List


def findContentChildren(g: List[int], s: List[int]) -> int:
    g.sort()
    s.sort()
    g_len, s_len = len(g), len(s)
    g_left = s_left = num_bist = 0
    while g_left < g_len and s_left < s_len:
        if g[g_left] <= s[s_left]:
            num_bist += 1
            g_left += 1
            s_left += 1
        else:
            s_left += 1
    return num_bist


def main():
    g = [1, 2, 3]
    s = [1, 1]
    print(findContentChildren(g, s))


if __name__ == '__main__':
    main()
