from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    ans = ''
    for i in zip(*strs):  # 解压strs
        if len(set(i)) == 1:
            ans += i[0]
        else:
            break
    return ans

def main():
    strs = ["cir", "car"]
    aa = longestCommonPrefix(strs)
    print(aa)

if __name__ == '__main__':
    main()