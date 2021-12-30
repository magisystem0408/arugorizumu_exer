
# 標準出力に関して
# https://qiita.com/zenrshon/items/c4f3849552348b3dbe67

# 3乗する
x = int(input())
print(x ** 3)

# 長方形の面積と周の長さ
a, b = map(int, input().split())
print(a * b, 2 * (a + b))

## 内包表記による回答
input = input()
a, b = [int(elem) for elem in input.split()]

print(a * b, 2 * (a + b))

# a,b,c,を入力したときa<b<cならばYesそれ以外ならfalse

input = input()
a, b, c = [int(elem) for elem in input.split()]

# ちなみに配列の表記の仕方
# a =list(map(int,input().split()))


if a < b < c:
    print("Yes")
else:
    print("No")

"""
長方形の中の円
"""

W, H, x, y, r = map(int, input().split())

if x >= r and x <= W - r and y >= r and y <= H - r:
    print("yes")
else:
    print("No")

"""
入力されてきた文字に対して、返答を返す
直し、0がきたらそこで終了する。
"""

case_num = 1
while True:
    tmp_num = int(input())
    if tmp_num == 0:
        break
    else:
        print("Case {}:".format(case_num), tmp_num)
        case_num += 1

"""
自分の回答
※enumrateはindexをつけてくれる
"""
a = list(map(int, input().split()))
for i, enum in enumerate(a):
    if enum == 0:
        break
    print("Case{}:".format(i + 1), enum)

"""
データセットをもったやつが入ってきて、x,yに格納する
もし、yがxより大きかったら、交換して、0がきたら終わる
"""

while True:
    tmp_num = input()
    x, y = [int(elem) for elem in tmp_num.split()]
    if x > y:
        x, y = y, x
    elif x == 0 and y == 0:
        break
    print(x, y)

"""
a,b,cを読み込み
aからbまでの整数の中に、cの約数がいくつあるかを求める
"""
COUNT = 0

input = input()
x, y, z = [int(elem) for elem in input.split()]

for i in range(x, y + 1):
    if z % i == 0:
        COUNT += 1

print(COUNT)

"""
aとbを読み込んで、
・a÷b
・a÷bの余り
・a÷b f：浮動小数点
"""

x, y = map(int, input().split())

print("%d %d %.5f" % (x / y, x % y, x / y))

while True:
    table = input().split()

    a = int(table[0])
    op = table[1]
    b = int(table[2])

    if op == '?':
        break

    if op == '+':
        print("%d" % (a + b))
    elif op == '-':
        print("%d" % (a - b))
    elif op == '/':
        print("%d" % (a / b))
    else:
        print("%d" % (a * b))
