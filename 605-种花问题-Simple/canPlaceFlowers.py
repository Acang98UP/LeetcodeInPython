from typing import List


def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    # 添加哨兵
    flowerbed = flowerbed + [0]
    result = 0
    i, length = 0, len(flowerbed) - 1
    while i < length:
        if flowerbed[i]:
            i += 2
        elif flowerbed[i + 1]:
            i += 3
        else:
            result += 1
            i += 2

    # 注意返回值的写法
    return result >= n


def main():
    flowerbed = [1, 0, 0, 0, 1]
    n = 1
    print(canPlaceFlowers(flowerbed, n))


if __name__ == '__main__':
    main()
