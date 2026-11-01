# 1. 讀取並以逗號切割輸入數值
n, a1, a2, a3 = map(int, input().split(','))

# 2. 計算水果總花費
total = a1 * 15 + a2 * 20 + a3 * 30

# 3. 判斷金額是否足夠並計算找零
if n < total:
    print('0')
else:
    change = n - total

    # 優先使用大面額（貪婪策略）
    coin_50 = change // 50
    change = change % 50

    coin_5 = change // 5
    change = change % 5

    coin_1 = change

    # 依序輸出 1 元、5 元、50 元的數量
    print(coin_1, coin_5, coin_50, sep=',')