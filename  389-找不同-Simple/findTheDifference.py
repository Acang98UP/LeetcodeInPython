def findTheDifference(s: str, t:str) ->str:
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