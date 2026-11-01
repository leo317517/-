"""
題目37：18啦遊戲設計 (18-Dice Game Logic - No Imports)
解題重點：
1. 透過 input() 逐行讀取 4 顆骰子點數，並以 try-except 捕捉 EOFError。
2. 使用 set(dice) 與 list.count() 原生語法統計點數頻率，避免引入外部套件。
3. 依據出現頻率 freq 進行條件分支：
   - [4]: 4 顆相同 -> 輸出 "WIN"
   - [3, 1] 或 [1, 1, 1, 1]: 3 顆相同或皆不相同 -> 輸出 "R"
   - [2, 2]: 兩組對子 -> 輸出 max(dice) * 2
   - [2, 1, 1]: 一組對子 -> 透過清單生成式找出 count 為 1 的兩顆骰子並加總
"""

while True:
    try:
        # 讀取 4 顆骰子的點數
        dice = []
        while len(dice) < 4:
            line = input().strip()
            if line:
                dice.append(int(line))

        # 計算各點數出現頻率並由大到小排序
        freq = sorted([dice.count(x) for x in set(dice)], reverse=True)

        # 1. 通殺
        if freq == [4]:
            print("WIN")

        # 2. 無意義
        elif freq == [3, 1] or freq == [1, 1, 1, 1]:
            print("R")

        # 3. 兩組對子：取點數較大的一組相加
        elif freq == [2, 2]:
            print(max(dice) * 2)

        # 4. 一組對子：計算另外兩顆獨立點數的和
        else:
            singles = [x for x in dice if dice.count(x) == 1]
            print(sum(singles))

    except EOFError:
        break