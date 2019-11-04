for i in range(100, 1000):
    for j in range(1, 10):
        if (i % j == 7) & int(i / j / 10) == 3 & ((int(i / j) - 30) * j >= 50) & ((int(i / j) - 30) * j < 60):
            if ((int(i / j) - 30) * j >= 50) & ((int(i / j) - 30) * j < 60):
                print(i, j)
