def insertionsort(A):
    for i in range (1, len(A)):
        # дальше сохраняем значение в новом элементе
        new_elem = A[i]
        # начианя с элемента А[i - 1]
        j = i - 1
        #все элементы которые больше нью элемента
        while j >= 0 and A[j] > new_elem:
            # сдыигаем вправо на + 1
            A[j + 1] = A[j]
            j -= 1
            #на своподное место записываем новый элемент
            A[j + 1] = new_elem

