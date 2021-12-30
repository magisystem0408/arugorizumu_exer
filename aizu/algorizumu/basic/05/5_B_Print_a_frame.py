# 最初と最後の処理をどうするか？

def main(height, width):
    for i in range(height - 1):
        if i == 0:
            print("#" * width)
        else:
            print("#" + "." * (width - 2) + "#")
    else:
        print("#" * width)
    print()


while True:
    H, W = [int(elem) for elem in input().split()]
    if H==0 and W==0:
        break
    main(H, W)
