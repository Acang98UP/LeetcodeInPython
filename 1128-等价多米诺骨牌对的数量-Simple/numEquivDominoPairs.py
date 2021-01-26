from typing import List


def numEquivDominoPairs(dominoes: List[List[int]]) -> int:
    if len(dominoes) == 1 or 0:
        return 0
    res = 0
    for i in range(0, len(dominoes)):
        for j in range(i + 1, len(dominoes)):
            if dominoes[i][0] == dominoes[j][0] and dominoes[i][1] == dominoes[j][1]:
                res += 1
            elif dominoes[i][0] == dominoes[j][1] or dominoes[i][1] == dominoes[j][0]:
                res += 1
    return res


def main():
    # dominoes = [[1, 2], [2, 1], [3, 4], [5, 6]]
    dominoes = [[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]
    print(numEquivDominoPairs(dominoes))



if __name__ == '__main__':
    main()