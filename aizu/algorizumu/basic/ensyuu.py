# 3で割り切れる時fizz
# 5で割り切れる時buzz
# 3 and 5で割り切れる時 fizzbuzz


for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('{}:FizzBuzz'.format(i))
    elif i % 3 == 0:
        print('{}:Fizz'.format(i))
    elif i % 5 == 0:
        print('{}:Buzz'.format(i))
    else:
        print(i)
