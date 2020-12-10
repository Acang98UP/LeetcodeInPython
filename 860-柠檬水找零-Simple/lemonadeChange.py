from typing import List
# 10th Dec

def lemonadeChange(bills: List[int]) -> bool:
    # p, q, r分别代表5, 10, 20元的数量
    p, q, r = 0, 0, 0
    for i in range(0, len(bills)):
        if bills[i] == 5:
            p += 1
            continue
        if bills[i] == 10:
            if p > 0:
                p -= 1
                q += 1
            else:
                return False
            continue
        if bills[i] == 20:
            if p >= 1 and q >= 1:
                r += 1
                p -= 1
                q -= 1
                continue
            if p > 3:
                p -= 3
                r += 1
                continue
            if q == 0 or p < 3:
                return False
    return True

def main():
    bills = [5,5,10,20,5,5,5,5,5,5,5,5,5,10,5,5,20,5,20,5]
    result = lemonadeChange(bills)
    print(result)

if __name__ == '__main__':
    main()