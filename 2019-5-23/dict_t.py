eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng2sp)
print(eng2sp['two'])
#print(eng2sp['four'])
print(len(eng2sp))
vals = eng2sp.values()
print(vals)

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    print(d)

histogram('banabdjjwqrtrteyrwjgcsuyerlkwqupotiu')

count = 0

def example():
    global count
    count += 1

example()
print(count)