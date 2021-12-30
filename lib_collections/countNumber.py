
d ={}
l=['a','a','a','b','b','c']

for word in l:
    if word not in d:
        d[word]=0
    d[word] +=1
print(d)
