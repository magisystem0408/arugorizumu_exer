import math


def is_prime_v1(num: int) -> bool:
    if num <= 1:
        return False

    # for i in range(2, num):
    #     if num % i == 0:
    #         return False

    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True


def is_prime_v2(num: int) -> bool:
    """
    36=1*36は36*1 の対象になってるものがある。
    これは√nを軸として対象になっている。
    """

    if num <= 1:
        return False

    for i in range(2, math.floor(math.sqrt(num) + 1)):
        if num % i == 0:
            return False

    return True


def is_prime_v3(num: int) -> bool:
    if num <= 1:
        return False

    if num == 2:
        return True

    # 後に続く偶数をバッサリきる
    if num % 2 == 0:
        return False

    # 奇数の場合だけを検証する
    for i in range(3, math.floor(math.sqrt(num) + 1), 2):
        if num % i == 0:
            return False
        i += 2
    return True


def is_prime_v4(num: int) -> bool:
    # 6k±1 <=√n
    if num <= 1:
        return False

    if num <= 3:
        return True

    if num % 2 == 0 or num % 3 == 0:
        return False

    for i in range(5, math.floor(math.sqrt(num) + 1), 6):
        if num % i == 0:
            return False


