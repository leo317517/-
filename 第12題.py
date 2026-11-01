# 1. 定義遞迴函式
def f(n):
    # 終止條件（Base Case）：當 n 為 0 或 1 時，直接回傳 n + 1
    if n == 0 or n == 1:
        return n + 1
    # 遞迴關係（Recursive Case）：拆解為兩個較小的子問題相加
    else:
        return f(n - 1) + f(n // 2)

# 2. 主程式：讀取輸入的整數 k
k = int(input())

# 3. 呼叫函式計算 f(k)
fk = f(k)

# 4. 輸出計算結果
print(fk)