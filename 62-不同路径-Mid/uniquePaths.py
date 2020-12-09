import math


def uniquePaths(m, n):
    return math.comb(m + n - 2, n - 1)

def main():
    m = int(input('m = '))
    n = int(input('n = '))
    ways = uniquePaths(m, n)
    print(ways)

if __name__ == '__main__':
    main()