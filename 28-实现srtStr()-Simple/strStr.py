def strStr(haystack: str, needle: str) -> str:
    length_hay = len(haystack)
    length_needle = len(needle)
    if length_needle == 0:
        return 0
    elif length_hay == 0 or length_needle > length_hay:
        return -1
    for i in range(0, length_hay - length_needle + 1):
        if haystack[i:i + length_needle] == needle:
            return i
    return -1

def main():
    haystack = ''
    needle = 'a'
    print(strStr(haystack, needle))

if __name__ == '__main__':
    main()