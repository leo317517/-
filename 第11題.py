while True:
    try:
        # 1. 讀取列數 R 與行數 C
        R, C = map(int, input().split())

        # 2. 階段一：讀入完整的二維矩陣
        matrix = []
        for _ in range(R):
            matrix.append(list(map(int, input().split())))

        # 3. 階段二：依序走訪直行 c，組裝並印出反轉後的列[cite: 6]
        for c in range(C):
            row = [matrix[r][c] for r in range(R)]
            print(*row)

    except EOFError:
        break