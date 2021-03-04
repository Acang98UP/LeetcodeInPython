from typing import List


def maxEnvelopes(envelopes: List[List[int]]) -> int:
    if len(envelopes) == 0:
        return 0
    envelopes = sorted(envelopes, key=lambda x: (x[0]))
    # print(envelops)
    res = [envelopes[0]]
    j = 0
    for i in range(1, len(envelopes)):
        if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
            res.append(envelopes[i])
            j = i
    print(envelopes)
    print(res)
    return len(res)


def main():
    # envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
    envelopes = [[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]
    print(maxEnvelopes(envelopes))


if __name__ == '__main__':
    main()