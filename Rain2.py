a_int = 0
summ = 0
while a_int < 5:
    b = int(input())
    if b == 0:
        a_int +=1
    elif a_int%2 !=0:
        summ +=b
print(summ)