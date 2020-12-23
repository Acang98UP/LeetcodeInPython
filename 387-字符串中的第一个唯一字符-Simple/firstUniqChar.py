import collections


def firstUniqChar(s: str) -> int:
    if len(s) == 0:
        return -1
    s_dict = collections.Counter(s)
    i = 0
    for i in range(0, len(s)):
        if s_dict[s[i]] != 1:
            continue
        else:
            return i
    return -1

def main():
    s = 'cc'
    print(firstUniqChar(s))

if __name__ == '__main__':
    main()