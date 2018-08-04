def linearSearch(intList,target):
    found = False
    position = 0
    while position < len(intList):
        if intList[position] == target:
            found = True
            break
        position = position + 1
    return found
linearList = [23,24,25,26,27,28,29,40]
numInput = int(input("что ты ищещь?\n"))
numFound = linearSearch(linearList,numInput)
if numFound:
    print("Оно есть")
else:
    print("Ты ошибся")