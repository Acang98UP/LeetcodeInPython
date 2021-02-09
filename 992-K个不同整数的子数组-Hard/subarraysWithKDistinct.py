from typing import List


def subarraysWithKDistinct(A: List[int], K: int) -> int:
    min_ptr = 0
    max_ptr = 0
    min_record_dict = {}
    max_record_dict = {}
    rst = 0
    for i in range(len(A)):
        if i == min_ptr:
            if A[i] not in min_record_dict:
                min_record_dict[A[i]] = 0
            min_record_dict[A[i]] += 1
            min_ptr += 1
        if i == max_ptr:
            if A[i] not in max_record_dict:
                max_record_dict[A[i]] = 0
            max_record_dict[A[i]] += 1
            max_ptr = i + 1
        while min_ptr < len(A) and len(min_record_dict) < K:
            if A[min_ptr] not in min_record_dict:
                min_record_dict[A[min_ptr]] = 0
            min_record_dict[A[min_ptr]] += 1
            min_ptr += 1
        while max_ptr < len(A) and len(max_record_dict) <= K:
            if A[max_ptr] not in max_record_dict:
                if len(max_record_dict) == K:
                    break
                max_record_dict[A[max_ptr]] = 0
            max_record_dict[A[max_ptr]] += 1
            max_ptr += 1
        if len(min_record_dict) < K:
            break
        rst += max_ptr - min_ptr + 1
        min_record_dict[A[i]] -= 1
        max_record_dict[A[i]] -= 1
        if min_record_dict[A[i]] == 0:
            del min_record_dict[A[i]]
        if max_record_dict[A[i]] == 0:
            del max_record_dict[A[i]]

    return rst


def main():
    A = [1, 2, 1, 2, 3]
    K = 2
    print(subarraysWithKDistinct(A, K))


if __name__ == '__main__':
    main()