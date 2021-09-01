def compareVersion(version1: str, version2: str) -> int:
    list1 = version1.split('.')
    list2 = version2.split('.')
    # 长度补齐
    if len(list1) > len(list2):
        for i in range(len(list1) - len(list2)):
            list2.append('0')
    else:
        for i in range(len(list2) - len(list1)):
            list1.append('0')
    # print(list1)
    # print(list2)
    # 逐一进行对比
    for i in range(len(list1)):
        if int(list1[i]) == int(list2[i]):
            continue
        elif int(list1[i]) > int(list2[i]):
            return 1
        elif int(list1[i]) < int(list2[i]):
            return -1
    # print(int(list1[1]) == int(list2[1]))
    return 0


if __name__ == '__main__':
    version1 = '7.5.2.4'
    version2 = '7.5.3'
    result = compareVersion(version1, version2)
    print(result)




