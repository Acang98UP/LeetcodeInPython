from typing import List


def splitIntoFibonacci(S: str) -> List[int]:
    split_Str = S.split(',')
    return split_Str

def main():
    s = "1123,5813"
    new_s = splitIntoFibonacci(s)
    print(new_s)
    s1 = 'zifuchuan'
    print(list(s))

if __name__ == '__main__':
    main()