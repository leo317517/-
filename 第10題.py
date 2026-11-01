def gcd(a, b):
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a

# 讀取輸入、計算並輸出結果
a, b = map(int, input().split())
ans = gcd(a, b)
print(ans)