def calculate(s: str) -> int:
    stack = []
    # 记录数字的符号, 因为题目说没有负数,说明第一个为正数,设为1
    sign = 1
    # 数字
    num = 0
    # 结果
    res = 0
    for c in s:
        if c.isdigit():
            num = num * 10 + int(c)
        elif c == "+":
            res += sign * num
            # 为下一次做准备
            num = 0
            sign = 1
        elif c == "-":
            res += sign * num
            # 为下一次做准备
            num = 0
            sign = -1
        elif c == "(":
            stack.append(res)
            stack.append(sign)
            sign = 1
            res = 0
        elif c == ")":
            res += sign * num
            num = 0
            res = stack.pop() * res + stack.pop()
    res += sign * num
    return res


def main():
    s = '1 + 1'
    print(calculate(s))


if __name__ == '__main__':
    main()