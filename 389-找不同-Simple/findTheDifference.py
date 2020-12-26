def findTheDifference(s: str, t:str) ->str:

    """
    ##比较两个字符的差集,统计每个字符中字符的个数
        countS = collections.Counter(s)
        countT = collections.Counter(t)
        # print(countS,countT)
        for val in countT:
            # print(val)
            if countT[val] != countS[val]:
                return val
    """

    if len(s) == 0:
        return t
    t = list(t)
    s = list(s)
    for i in range(0, len(s)):
        t.remove(s[i])
    return t[0]

def main():
    s = 'ae'
    t = 'aea'
    print(findTheDifference(s, t))

if __name__ == '__main__':
    main()