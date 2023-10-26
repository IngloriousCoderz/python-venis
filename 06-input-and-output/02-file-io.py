# -*- coding: utf-8 -*-

f = open('students.csv', 'r', encoding="utf-8")
data = f.read()
print(data)
print(f.closed)
f.close()
print(f.closed)

f = open('students.csv', 'rb')
data = f.read()
print(data)
print(data.decode(encoding="utf-8"))
f.close()

with open('students.csv', 'r', encoding="utf-8") as f:
    # data = f.read()
    # print(data)
    # print(list(f))
    # print(f.readlines())
    print(f.readline())
    for line in f:
        print(line, end='')
print(f.closed)
# f.read()

with open('students.csv', 'a', encoding="utf-8") as f:
    f.write('Neville Longbottom\n')
