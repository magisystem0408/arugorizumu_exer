from typing import List
A=['END']

def main(l:List):
    print(l)

    if l[0] ==0:
        # ここで挿入する
        print()
    elif l[0] ==1:
        print()
    else:
        print()

if __name__ == '__main__':
    N = int(input())
    for _ in range(N):
        l =list(map(int,input().split()))
        main(l)

    for elem in A:
        print(elem.join())