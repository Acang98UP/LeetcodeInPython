from typing import List


def wiggleMaxLength(nums: List[int]) -> int:
    # c是用来记录前一个差值是下降还是上升的，默认0
    n, c, res = len(nums), 0, 1
    if n < 2:
        return n
    for i in range(1, n):
        x = nums[i] - nums[i - 1]
        # 如果有差值才继续处理，相等直接就跳过不处理了
        if x:
            # <0代表有上升下降的交替，=0是初始情况的判断
            if x * c <= 0:
                res += 1
            c = x
    return res

def main():
    testSequence = [1, 7, 4, 9, 2, 5]
    print(wiggleMaxLength(testSequence))


if __name__ == '__main__':
    main()