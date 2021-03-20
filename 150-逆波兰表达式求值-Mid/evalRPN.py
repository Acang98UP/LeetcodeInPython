from typing import List


def evalRPN(tokens: List[str]) -> int:
    # 后序表达式的输出
    if len(tokens) == 0:
        return 0
    elif len(tokens) == 1:
        return int(tokens[0])
    stack = []
    logo = ['+', '-', '*', '/']
    i = 0
    while i != len(tokens):
        if tokens[i] in logo:
            num2, num1 = stack.pop(-1), stack.pop(-1)
            if tokens[i] == '+':
                stack.append(num1 + num2)
            elif tokens[i] == '-':
                stack.append(num1 - num2)
            elif tokens[i] == '*':
                stack.append(num1 * num2)
            elif tokens[i] == '/':
                stack.append(int(num1 / num2))
            i += 1
        else:
            stack.append(int(tokens[i]))
            i += 1
    return stack[-1]

def main():
    # tokens = ["2", "1", "+", "3", "*"]
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(evalRPN(tokens))


if __name__ == '__main__':
    main()