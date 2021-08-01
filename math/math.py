import numpy as np
"""
sin cosの定義
"""

def mysin(x):
    return np.sin(x)


def my_cos(x):
    return np.cos(x)



"""
総乗
"""

a =np.array([1,3,2,5,3])
y =a.prod(a)

print(y)

"""
乱数
"""


r =np.random.randint(6)+1
print(r)
