from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    dic = {}
    res =[]
    for i in strs:
      dic.setdefault(str(sorted(i)), []).append(i)
    for value in dic.values():
      res.append(value)
    return res

    # 利用好list里面的方法setdefault()方法
    # 字符串有sort() 方法就可以顺利解决乱序的问题

def main():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(groupAnagrams(strs))

if __name__ == '__main__':
    main()