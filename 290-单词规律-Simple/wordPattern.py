
def wordPattern(pattern: str, s: str) -> bool:
    wordDict = {}
    new_s = s.split(" ")
    value = []
    list_patten = list(pattern)
    if len(pattern) != len(new_s):
        return False
    for i in range(0, len(pattern)):
        if list_patten[i] in wordDict:
            if new_s[i] == wordDict[list_patten[i]]:
                continue
            else:
                return False
        else:
            # 此时要保证字典值的唯一性
            if new_s[i] in value:
                return False
            else:
                value.append(new_s[i])
                wordDict[list_patten[i]] = new_s[i]
    return True

def main():
    pattern = "abba"
    s = "dog dog dog dog"
    print(wordPattern(pattern, s))


if __name__ == '__main__':
    main()