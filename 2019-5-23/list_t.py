cheeses = ['Cheddar', 'Edam', 'Gouda']
numbers = [42, 123]
empty = ['xiaomi', 25 , 'male']
numbers[1] = 87
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
a = empty + numbers  #list pinjie
print(cheeses, numbers, empty)
print(cheeses[0],a)
print(a * 4)  #list repeat

print(a[::-1])  #qiepian shixian list fanzhuan

print(sum(numbers))

#delete one in list
#fangfa 1
x = cheeses.pop()
print(cheeses, x)

#fangfa 2
del a[1]
print(a)
del a[1:]
print(a)

#fangfa 3
empty.remove('male')
print(empty)

print(list(a[0])) 

b = 'xiaomi'
c = 'xiaomi'
print(b is c)
b = [1, 2, 3]
c = [1, 2, 3]
print(b is c)
b = [1, 2, 3]
c = b
print(b is c)

t = [[1,2], [3], [4, 5, 6]]
sum_t = 0
for i in range(len(t)):
    sum_t += sum(t[i])
print(sum_t)

t = [1, 2, 3]
T = []
for i in range(len(t)):
    su = 0
    #print(i)
    while i >= 0:
        su += t[i]
        i = i -1
    T.append(su)
print(T)