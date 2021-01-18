from typing import List


class UnionFind:
    def __init__(self):
        self.father = {}
        # 根节点所在集合的所有账户
        self.accounts = {}

    def find(self, x):
        if not self.father[x]:
            return x

        # 递归的路径压缩处理
        self.father[x] = self.find(self.father[x])

        return self.father[x]

    def merge(self, x, y):
        root_x, root_y = self.find(x), self.find(y)

        if root_x == root_y:
            return

        # 按秩合并，更新根节点和所属的账户
        if len(self.accounts[root_x]) > len(self.accounts[root_y]):
            self.father[root_y] = root_x
            self.accounts[root_x] += self.accounts[root_y]
            del self.accounts[root_y]
        else:
            self.father[root_x] = root_y
            self.accounts[root_y] += self.accounts[root_x]
            del self.accounts[root_x]

    def add(self, x):
        if x not in self.father:
            self.father[x] = None
            self.accounts[x] = [x]


def accountsMerge(accounts: List[List[str]]) -> List[List[str]]:
    uf = UnionFind()
    for account in accounts:
        # 找到姓名和主账户
        name, master = account[0], account[1]
        uf.add((name, master))

        # 和其余的账户一一合并
        account = list(set(account[2:]))
        for i in range(len(account)):
            uf.add((name, account[i]))
            uf.merge((name, master), (name, account[i]))

    res = []
    for key, value in uf.father.items():
        # 是根节点
        if not value:
            # 添加user
            usr_account = [uf.accounts[key][0][0]]
            # 添加账户
            for account in uf.accounts[key]:
                usr_account.append(account[1])

            res.append(sorted(usr_account))

    return res


def main():
    accounts = [["John", "johnsmith@mail.com", "john00@mail.com"],
                ["John", "johnnybravo@mail.com"],
                ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                ["Mary", "mary@mail.com"]]
    print(accountsMerge(accounts))


if __name__ == '__main__':
    main()