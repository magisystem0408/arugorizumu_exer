# Input:'This is a pen. This is an apple. Applepen.'
# output:('p',6)
from typing import Any

from collections import Counter
import operator
from typing import Tuple

def count_chars_v1(string:str) ->Tuple[str,int]:
    strings =string.lower()
    l=[]
    for char in strings:
        if not char.isspace():
            l.append((char,strings.count(char)))

    # リスト内包括で書いた時
    # l =[(c,strings.count(c)) for c in strings if not c.isspace()]
    return max(l,key=operator.itemgetter(1))


def count_chars_v2(strings:str) ->Tuple[str,int]:
    strings =strings.lower()
    d ={}
    for char in strings:
        if not char.isspace():
            d[char] =d.get(char,0)+1
    max_key =max(d,key=d.get)
    return max_key,d[max_key]


def count_chars_v3(strings:str) ->Tuple[str,int]:
    strings =strings.lower()
    d =Counter()
    for char in strings:
        if not char.isspace():
            d[char] +=1
    max_key =max(d,key=d.get)
    return max_key,d[max_key]



if __name__ == '__main__':
    t='This is a pen. This is an apple. Applepen.'
    print(count_chars_v1(t))