from typing import List

# これがtに応じて存在する
A = []
A = []


def main(l: List):
    if l[0] == 0:
        print()
    elif l[0] == 1:
        print()
    else:
        print()


if __name__ == '__main__':
    test = input()
    N, M = [int(elem) for elem in test.split()]
    for _ in range(M):
        l = list(map(int, input().split()))
        print(l)
