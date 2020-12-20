def removeKdigits(num: str, k: int) -> str:
    stack = []
    remain = len(num) - k
    for i in num:
        # 此处的思路借鉴316，都是用stack来存放最终的结果，这样就可以保证相对位置的不变
        while k and stack and stack[-1] > i:
            stack.pop()
            k -= 1
        stack.append(i)
    return ''.join(stack[:remain]).lstrip('0') or '0'

def main():
    num = '1432219'
    print(removeKdigits(num, 3))

if __name__ == '__main__':
    main()