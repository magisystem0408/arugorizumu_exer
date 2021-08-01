import random

from typing import List


# シャッフルした後順序通りに並んでいるか確認する

def in_order(numbers:List[int]) ->bool:
    # 一個前
    # for i in range(len(numbers)-1):
    #     if numbers[i]>numbers[i+1]:
    #         return False
    #
    # return True


    # リスト内包括になる
    # allは全てtrueであれば
    return all(numbers[i] <= numbers[i + 1] for i in range(len(numbers) - 1))


def bogo_sort(numbers:List[int])->List[int]:
    while not in_order(numbers):
        random.shuffle(numbers)
    print(numbers)


if __name__ == '__main__':
    num = [random.randint(0, 100) for _ in range(10)]
