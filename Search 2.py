arr = list(map(int,input().split()))
m1 = arr[0]
m2 = arr[0]
for elem in arr:
    if elem > m1:
        m1 = m2
        m1 = elem
    elif (elem > m2) and (elem != m1): # проверка что бы не нашло одно и то же число
        m2 = elem
print (m1, m2)