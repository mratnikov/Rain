Stack = []
def push(val):
    Stack.append(val)
def pop():
    return Stack.pop()
def top():
    return Stack[-1]
def size():
    return len(Stack)
def isempty():
    return len(Stack) == 0
def clear():
    Stack[:] = []
