def move(n, start, finish):
    if n > 0:
        temp = 6 — start — finish
        move(n — 1, start, temp)
        print("Перенести диск", n, "со стержня", start, "на стержень", finish)
        move(n — 1, temp, finish)
