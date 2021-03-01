from typing import List


def isMonotonic(A: List[int]) -> bool:
    N = len(A)
    inc, dec = True, True
    for i in range(1, N):
        if A[i] < A[i - 1]:
            inc = False
        if A[i] > A[i - 1]:
            dec = False
        if not inc and not dec:
            return False
    return True


def main():
    A = [11, 11, 9, 4, 3, 3, 3, 1, -1, -1, 3, 3, 3, 5, 5, 5]
    print(isMonotonic(A))


if __name__ == '__main__':
    main()