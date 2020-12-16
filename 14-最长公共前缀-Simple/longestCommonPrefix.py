from typing import List


def longestCommonPrefix(strs: List[str]) -> str:

    if len(strs) == 0:
        return ''
    str_List = []
    min = 100000
    for i in range(0, len(strs)):
        temp = list(strs[i])
        if len(temp) < min:
            min = len(temp)
        str_List.append(temp)
    return_str = ''
    index = 0
    for i in range(0, min):  # i是总共对比的位数
        for j in range(1, len(str_List)):  # j是每次对比的数，从第二个字符串开始计数
            while str_List[j][index] != str_List[0][index]:
                return return_str
            else:
                j += 1
        return_str += str_List[0][i]
        index = i + 1
    return return_str

def main():
    strs = ["cir", "car"]
    aa = longestCommonPrefix(strs)
    print(aa)

if __name__ == '__main__':
    main()