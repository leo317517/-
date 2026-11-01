
while True:
    try:
        n = int(input().strip())
        # 每一段的 (容量, 夏月單價, 非夏月單價)
        tiers = [
            (120, 2.10, 2.10),  # 120 度以下
            (210, 3.02, 2.68),  # 121-330 度 (容量 210 度)[cite: 2]
            (170, 4.39, 3.61),  # 331-500 度 (容量 170 度)[cite: 2]
            (200, 4.97, 4.01),  # 501-700 度 (容量 200 度)[cite: 2]
        ]
        summer_cost = 0.0
        non_summer_cost = 0.0
        remaining = n  # 輸入的總度數

        for cap, s_rate, ns_rate in tiers:
            #多元組解包（Tuple Unpacking）：依序取出 tiers 串列中的每一個階梯資料。每一輪會將該段的「容量上限 🪣」指派給 cap、「夏月單價 ☀️」指派給 s_rate、「非夏月單價 ❄️」指派給 ns_rate。
            used = min(remaining, cap)
            #計算當前階梯使用的度數：利用 min() 找出「剩餘度數」與「該段容量上限」的較小值。如果剩餘度數大於容量，就裝滿該段容量；如果剩餘度數比較小（或已經為 0），就只計算剩下來的度數。
            summer_cost += used * s_rate
            non_summer_cost += used * ns_rate
            remaining -= used

        summer_cost += remaining * 5.63
        non_summer_cost += remaining * 4.50

        print(f"Summer months:{summer_cost:.2f}")
        print(f"Non-Summer months:{non_summer_cost:.2f}")

    except EOFError:
        break