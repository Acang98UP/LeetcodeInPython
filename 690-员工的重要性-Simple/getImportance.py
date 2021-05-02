# Definition for Employee.
from typing import List

class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


def getImportance(self, employees: List['Employee'], id: int) -> int:
    i = 0
    # dfs


def main():
    employees = [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]]
    id = 1
    print(getImportance(employees, id))


if __name__ == '__main__':
    main()





