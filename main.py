def primeNumber(num):
    for i in range(1, num):
        if num % i == 0:
            return i

if __name__ == '__main__':
    input = int(input())

    print(primeNumber(input))
