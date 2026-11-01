# 題目40：ISBN驗證 (ISBN Verification)
# 核心邏輯：字元轉換 -> 兩階段原地前綴和 -> 模 11 驗證

while True:
    try:
        # 1. 讀取並以空格切分字串
        raw_tokens = input().split()
        if not raw_tokens:
            continue

        # 2. 字元轉整數：遇 'X' 或 'x' 轉換為 10，其餘轉為 int
        nums = [10 if x.upper() == "X" else int(x) for x in raw_tokens]

        # 3. 執行兩次原地前綴和累加
        for _ in range(2):
            for i in range(1, 10):
                nums[i] += nums[i - 1]

        # 4. 判斷識別碼（最後一格）是否為 11 的倍數
        if nums[-1] % 11 == 0:
            print("YES")
        else:
            print("NO")

    except EOFError:
        break