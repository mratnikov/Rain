Queue = []
def push(val):
    Queue.append(val)
def pop():
    global QueueStart
    result = Queue[QueueStart]
    QueueStart += 1
    if QueueStart > len(Queue) / 2:
        Queue[:QueueStart] = []
        QueueStart = 0
    return result
def top():
    return Queue[0]
def size():
    return len(Queue)
def isempty():
    return len(Queue) == 0
def clear():
    Queue[:] = []

