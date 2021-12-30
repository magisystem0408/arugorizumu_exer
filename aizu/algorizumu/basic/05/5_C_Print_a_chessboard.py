# チェスボードの描画について

def main(height, width):
    for i in range(height):
        if i % 2 == 0:
            d = []
            for j in range(width):
                if j % 2 == 0:
                    d.append("#")
                else:
                    d.append(".")
            print("".join(map(str, d)))

        else:
            d = []
            for j in range(width):
                if j % 2 == 0:
                    d.append(".")
                else:
                    d.append("#")
            print("".join(map(str, d)))
    print()


while True:
    H, W = [int(elem) for elem in input().split()]
    if H == 0 and W == 0:
        break
    main(H, W)
