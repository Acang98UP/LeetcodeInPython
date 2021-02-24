from typing import List


def maxSatisfied(customers: List[int], grumpy: List[int], X: int) -> int:
    N = len(customers)
    sum_ = 0
    # 所有不生气时间内的顾客总数
    for i in range(N):
        sum_ += customers[i] * (1 - grumpy[i])
    # 生气的 X 分钟内，会让多少顾客不满意
    curValue = 0
    # 先计算起始的 [0, X) 区间
    for i in range(X):
        curValue += customers[i] * grumpy[i]
    resValue = curValue
    # 然后利用滑动窗口，每次向右移动一步
    for i in range(X, N):
        # 如果新进入窗口的元素是生气的，累加不满意的顾客到滑动窗口中
        # 如果离开窗口的元素是生气的，则从滑动窗口中减去该不满意的顾客数
        curValue = curValue + customers[i] * grumpy[i] - customers[i - X] * grumpy[i - X]
        # 求所有窗口内不满意顾客的最大值
        resValue = max(resValue, curValue)
    # 最终结果是：不生气时的顾客总数 + 窗口X内挽留的因为生气被赶走的顾客数
    return sum_ + resValue


def main():
    customers = [1, 0, 1, 2, 1, 1, 7, 5]
    grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
    X = 3
    print(maxSatisfied(customers, grumpy, X))


if __name__ == '__main__':
    main()