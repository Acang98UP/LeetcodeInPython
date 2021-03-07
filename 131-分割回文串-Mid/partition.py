from typing import List


def partition(s: str) -> List[List[int]]:
    isPalindrome = lambda s: s == s[::-1]
    res = []
    backtrack(s, res, [])
    return res


def backtrack(self, s, res, path):
    if not s:
        res.append(path)
        return
    for i in range(1, len(s) + 1):  # 注意起始和结束位置
        if self.isPalindrome(s[:i]):
            self.backtrack(s[i:], res, path + [s[:i]])


def main():
    s = 'aab'
    print(partition(s))


if __name__ == '__main__':
    main()