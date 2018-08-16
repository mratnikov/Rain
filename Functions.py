def f():
    global a
    a = 1
    print(a)
a = 0
f()
print(a)
