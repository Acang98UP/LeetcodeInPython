from typing import List


def largestRectangleArea(heights: List[int]) -> int:
    stack = []
    heights = [0] + heights + [0]
    result = 0
    for i in range(len(heights)):
        while stack and heights[stack[-1]] > heights[i]:
            tmp = stack.pop()
            result = max(result, (i - stack[-1] - 1) * heights[tmp])
        stack.append(i)
    return result

def main():
    heights = [2, 1, 5, 6, 2, 3]
    print(largestRectangleArea(heights))

if __name__ == '__main__':
    main()