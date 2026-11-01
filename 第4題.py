# 1. 讀取開始與結束時間
start_hour, start_minute = map(int, input().split())
end_hour, end_minute = map(int, input().split())

# 2. 將時間換算成分鐘
start_minutes = start_hour * 60 + start_minute
end_minutes = end_hour * 60 + end_minute

# 3. 計算停車總分鐘數
total_minutes = end_minutes - start_minutes

# 4. 計算完整半小時數
half_hours = total_minutes // 30

# 5. 使用 if、elif、else 計算停車費
if half_hours <= 4:
    fee = half_hours * 30
elif half_hours <= 8:
    fee = 30 * 4 + (half_hours - 4) * 40
else:
    fee = 30 * 4 + 40 * 4 + (half_hours - 8) * 60


# 6. 輸出結果
print(fee)