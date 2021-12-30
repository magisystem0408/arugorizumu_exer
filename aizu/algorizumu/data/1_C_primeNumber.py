count = 0
while True:
    num = int(input())
    flag = False
    for i in range(2, num - 1):
        if num % i == 0:
            flag = True
            break

    if not flag:
        count += 1
    print(count)
