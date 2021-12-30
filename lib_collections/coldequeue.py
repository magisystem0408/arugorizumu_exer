# dequeの使い道
# https://note.nkmk.me/python-collections-deque/


# 要素の追加・取り出し(削除)・アクセスが両端のみ→queue
# 両端以外の要素に頻繁にアクセス→リスト

from collections import deque


d =deque()

d.append("test")
d.appendleft("mamushi")

# 末尾に追加される
d.extend(["test","aaaa"])

# 要素が反転されて、前に付け加えられる
d.extendleft(["mamushi","timineko"])

print(d)
# 実行結果
# deque(['timineko', 'mamushi', 'mamushi', 'test', 'test', 'aaaa'])