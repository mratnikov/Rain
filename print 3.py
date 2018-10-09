[[m * i + j * (i % 2 == 0) + (m - 1 - j) * (i % 2 == 1) for j in range(m)] for i in range(n)]
