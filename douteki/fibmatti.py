"""フィボナッチ数列の実装"""


def factorial(first, last, count):
    list = [first, last]
    for i in range(1, count):
        list.append(list[i - 1] + list[i])
    print(list[35])
    print(list)


# 分割統治法だと無駄な計算ができてしまう
# フィボナッチ数列は、n項目はn-1項目とn-2項目の和で計算できる
def fib(n):
    """1番目と2番目は1が帰ってくる"""
    if n == 0 or n == 1:
        return 1
    return fib(n - 1) + fib(n + 2)


# 動的計画法で処理する
# 同じ計算結果はmemoに入れて再利用するようにする


def fib_memo(n):
    memo = [None] * (n + 1)

    def _fib(n):
        if n == 0 or n == 1:
            return 1
        if memo[n] != None:
            return memo[n]
        memo[n] = _fib(n - 1) + _fib(n - 2)
        return memo[n]

    return _fib(n)


if __name__ == '__main__':
    # factorial(1, 1, 35)

    for i in range(35):
        print(fib_memo(i))
