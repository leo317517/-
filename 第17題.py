# 1. 讀取輸入、轉全小寫並依照空格切分
words = input().lower().split()

result = []

# 2. 逐一檢查並保留未出現過的單字（保留原始順序）
for word in words:
    if word not in result:
        result.append(word)

# 3. 解包清單，以預設空格隔開輸出並換行
print(*result)