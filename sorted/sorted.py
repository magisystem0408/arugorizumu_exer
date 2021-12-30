# 偶数奇数並べ替え

# [1,2,3,4,2,4,5,1,6,9,8,]
# を偶数奇数ならべ変による

from typing import List


# 新しい配列を作るパターン
def order_even_first_odd_last_v1(numbers: List[int]) -> None:
    even_list, odd_list = [], []
    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)
    numbers[:] = even_list + odd_list


def order_even_first_odd_last_v2(numbers: List[int]) -> None:
    # len(numbers)-1でリストの一番最後
    i, j = 0, len(numbers) - 1
    while i < j:
        if numbers[i] % 2 == 0:
            i += 1
        else:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            j -= 1

        # print(numbers)


if __name__ == '__main__':
    l = [0, 1, 3, 4, 2, 4, 1, 6, 8, 9, 8]
    order_even_first_odd_last_v1(l)

