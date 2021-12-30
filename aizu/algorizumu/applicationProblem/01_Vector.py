A = []


def main(l):
    if l[0] == 0:
        A.append(l[1])
    elif l[0] == 1:
        print(A[l[1]])
    else:
        A.pop()


if __name__ == '__main__':
    N = int(input())
    for _ in range(N):
        l = list(map(int, input().split()))
        main(l)
