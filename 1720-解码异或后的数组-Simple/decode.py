from typing import List


def decode(encoded: List[int], first: int) -> List[int]:
    n = len(encoded)
    arr = [first] + [0] * n
    for i in range(n):
        arr[i + 1] = encoded[i] ^ arr[i]
    return arr


def main():
    encoded = [1, 2, 3]
    first = 1
    print(decode(encoded, first))


if __name__ == '__main__':
    main()




