class MyQueue:

    stack1 = []

    def __init__(self):
        # 初始化队列
        self.stack1 = []

    def push(self, x: int) -> None:
        # 将元素放在队列之尾
        self.stack1.append(x)

    def pop(self) -> int:
        # 移除队列第一个元素，并返回
        try:
            temp = self.stack1[0]
            self.stack1 = self.stack1[1:]
            return temp
        except ValueError:
            print("Error")

    def peek(self) -> int:
        # 返回第一个元素
        try:
            temp = self.stack1[0]
            return temp
        except ValueError:
            print("Error")

    def empty(self) -> bool:
        # 判断队列是否为空
        return len(self.stack1) == 0

