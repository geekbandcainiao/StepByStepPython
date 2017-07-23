print(ord('A'))

print(ord('中'))

print('\u4e2d\u6587')

print(len('ABC'))

print('%2d-%02d' % (3,1))

print('%.2f' % 3.1415926)

classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)

print(classmates[0])

print(classmates[-2])

classmates.append('Adam')
print(classmates)

classmates.insert(1, 'Jack')
print(classmates)

classmates.pop()
print(classmates)

classmates.pop(1)
print(classmates)

classmates[1] = 'Sarah'
print(classmates)

L = ['Apple', 123, True]
print(L)

s = ['python', 'java', ['asp', 'php'], 'scheme']
print(s)

L = []
print(L)

classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)

t = (1, 2)
print(t)

t = ('a', 'b', ['A', 'B'])
print(t)

t[2][0] = 'X'
t[2][1] = 'Y'
print(t)



L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print(L[0][0])
print(L[1][1])
print(L[2][2])

