from typing import List


def numEquivDominoPairs(dominoes: List[List[int]]) -> int:
    if len(dominoes) == 0 or len(dominoes[0]) == 0:
        return 0

    pairNum = 0

    for i in range(len(dominoes) - 1):
        cnt = 0
        if i >= len(dominoes):  # 因为我们有删除操作，所以dominoes的长度小了，i会超出索引值
            break
        for j in range(len(dominoes) - 1, i, -1):  # 从最后一张牌向前遍历，直到i+1
            if dominoes[i][0] == dominoes[j][0] and dominoes[i][1] == dominoes[j][1]:
                cnt += 1
                del dominoes[j]
            elif dominoes[i][0] == dominoes[j][1] and dominoes[i][1] == dominoes[j][0]:
                cnt += 1
                del dominoes[j]
        pairNum += int(cnt * (cnt + 1) / 2)
    return pairNum


def main():
    # dominoes = [[1, 2], [2, 1], [3, 4], [5, 6]]
    dominoes = [[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]
    print(numEquivDominoPairs(dominoes))


if __name__ == '__main__':
    main()