op_count = 0

for n in {10,100,1000, 5000}:
    s = 0
    for i in range (n):
        s +=i
        op_count +=1
print (n, s, op_count)

