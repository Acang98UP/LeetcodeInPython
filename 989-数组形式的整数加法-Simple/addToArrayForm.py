from typing import List


def addToArrayForm(A: List[int], K: int) -> List[int]:
    i = len(A) - 1
    while K:
        A[i] += K
        K, A[i] = A[i] // 10, A[i] % 10
        i -= 1

        if i < 0 and K:
            A.insert(0, 0)
            i = 0
    return A


def main():
    A = [2, 1, 5]
    K = 806
    print(addToArrayForm(A, K))


if __name__ == '__main__':
    main()