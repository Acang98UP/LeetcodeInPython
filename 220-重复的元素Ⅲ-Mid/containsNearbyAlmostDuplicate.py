import bisect
from typing import List


def containsNearbyAlmostDuplicate(nums: List[int], k: int, t: int) -> bool:
    from sortedcontainers import SortedSet
    st = SortedSet()
    left, right = 0, 0
    res = 0
    while right < len(nums):
        if right - left > k:
            st.remove(nums[left])
            left += 1
        index = bisect.bisect_left(st, nums[right] - t)
        if st and 0 <= index < len(st) and abs(st[index] - nums[right]) <= t:
            return True
        st.add(nums[right])
        right += 1
    return False


def main():
    nums = [1, 2, 3, 1]
    k = 3
    t = 0
    print(containsNearbyAlmostDuplicate(nums, k, t))


if __name__ == '__main__':
    main()