from typing import List


def maxTurbulenceSize(arr: List[int]) -> int:
    N = len(arr)
    up = [1] * N
    down = [1] * N
    res = 1
    for i in range(1, N):
        if arr[i - 1] < arr[i]:
            up[i] = down[i - 1] + 1
        elif arr[i - 1] > arr[i]:
            down[i] = up[i - 1] + 1
        res = max(res, max(up[i], down[i]))
    return res


def main():
    arr = [9, 4, 2, 10, 7, 8, 8, 1, 9]
    print(maxTurbulenceSize(arr))


if __name__ == '__main__':
    main()