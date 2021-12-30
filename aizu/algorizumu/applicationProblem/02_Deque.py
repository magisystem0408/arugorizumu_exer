N = int(input())
A = []
for _ in range(N):
    x = list(map(int, input().split()))
    if x[0] == 0:
        if x[1] == 0:
            A.insert(0, x[2])
        else:
            A.append(x[2])
    elif x[0] == 1:
        print(A[x[1]])
    else:
        if x[1] == 0:
            A.pop(0)
        else:
            A.pop()
