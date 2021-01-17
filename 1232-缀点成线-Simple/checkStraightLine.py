from typing import List


def checkStraightLine(coordinates: List[List[int]]) -> bool:
    # if len(coordinates) == 2:
    #     return True
    # stack = []
    # for i in range(1, len(coordinates)):
    #     fenmu = coordinates[i][0] - coordinates[i - 1][0]
    #     if fenmu == 0 and stack is not None:
    #         return False
    #     else:
    #         continue
    #     temp = (coordinates[i][1] - coordinates[i - 1][1]) / fenmu
    #     if stack and temp != stack[-1]:
    #         return False
    #     else:
    #         stack.append(temp)
    # return True
    flag = True
    for i in range(len(coordinates) - 2):
        k1 = (coordinates[i][1] - coordinates[i + 1][1]) * (coordinates[i + 1][0] - coordinates[i + 2][0])
        k2 = (coordinates[i + 1][1] - coordinates[i + 2][1]) * (coordinates[i][0] - coordinates[i + 1][0])
        if k1 != k2:
            flag = False
            break
    return flag


def main():
    # coordinates = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
    # coordinates = [[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]
    coordinates = [[0, 0], [0, 1], [0, -1]]
    print(checkStraightLine(coordinates))


if __name__ == '__main__':
    main()