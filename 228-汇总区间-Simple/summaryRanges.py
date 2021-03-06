from typing import List


def summaryRages(nums: List[int]) -> List[str]:
    if len(nums) == 0:
        return []
    elif len(nums) == 1:
        return [str(nums[0])]
    result = []
    j = 0
    for i in range(len(nums)):
        if i:
            if nums[i] - nums[i - 1] != 1:
                if j == i - 1:
                    result.append(str(nums[j]))
                else:
                    result.append(str(nums[j]) + '->' + str(nums[i - 1]))
                if i == len(nums) - 1:
                    result.append(str(nums[i]))
                j = i
        if i == len(nums) - 1 and j < len(nums) - 1:
            result.append(str(nums[j]) + '->' + str(nums[i]))
    return result


def main():
    nums = [0, 1, 2, 4, 5, 7]
    print(summaryRages(nums))


if __name__ == '__main__':
    main()