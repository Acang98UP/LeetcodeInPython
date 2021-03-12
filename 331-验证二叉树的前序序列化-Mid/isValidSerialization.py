def isValidSerialization(preorder: str) -> bool:
    num = 1
    for i in preorder.split(','):
        if num == 0:
            return False
        if i == '#':
            num -= 1
        else:
            num += 1
    return num == 0


def main():
    preorder = '9,3,4,#,#,1,#,#,2,#,6,#,#'
    print(isValidSerialization(preorder))


if __name__ == '__main__':
    main()