from typing import List


def predictPartyVictory(senate: str) -> str:
    splited_str = list(senate)  # 将输入的字符串拆分成一个一个的字符“人”
    R_List = []  # 用于存放Radiant阵营的人的序列
    D_List = []  # 用于存放Dire阵营的人的序列
    for i in range(0, len(splited_str)):  # 遍历存放序号
        if splited_str[i] == 'R':
            R_List.append(i)
        else :
            D_List.append(i)
    if len(R_List) != 0 and len(D_List) != 0: # 判断是不是有一方没有人
        R_Index, D_Index = 0, 0
        while len(R_List) != 0 and len(D_List) != 0:  # 如果有人，进行人员数量动态检测
            for x in splited_str:
                if x == 'R':
                    if D_Index >= len(D_List):
                        D_Index = 0
                    splited_str.pop(D_List[D_Index])
                    D_List.pop(D_Index)
                    if R_Index < len(R_List):
                        R_Index += 1
                    else :
                        R_Index = 0
                elif x == 'D':
                    if R_Index >= len(R_List):
                        R_Index = 0
                    splited_str.pop(R_List[R_Index])
                    R_List.pop(R_Index)
                    if D_Index < len(D_List):
                        D_Index += 1
                    else :
                        D_Index = 0
    if len(R_List) == 0:
        return 'Dire'
    else:
        return 'Radiant'

def main():
    senate = "DDRRR"
    print(predictPartyVictory(senate))

if __name__ == '__main__':
    main()

# senate = "RDD"
# print(list(senate))