# 素数生成

from typing import List, Generator


def generate_primes_v1(number: int) -> List[int]:
    primes = []
    for x in range(2, number + 1):
        for y in range(2, x):
            if x % y == 0:
                break
        # 最後まで実行させるために、for-else
        else:
            primes.append(x)
    return primes


# 倍数にひっかからなければいい
def generate_primes_v2(number: int) -> List[int]:
    primes = []
    cache = {}
    for x in range(2, number + 1):
        if (is_prime := cache.get(x)) is False:
            continue
        primes.append(x)
        cache[x] = True
        for y in range(x * 2, number + 1, x):
            cache[y] = False
    return primes


def generate_primes_v3(number: int) -> Generator[int, None, None]:
    cache = {}
    for x in range(2, number + 1):
        if (is_prime := cache.get(x)) is False:
            continue
        yield x
        cache[x] = True
        for y in range(x * 2, number + 1, x):
            cache[y] = False

if __name__ == '__main__':
    print(generate_primes_v2(50))


