"""
題目26：各位數和排序 (Sum of Digits Sorting)
解題重點：
1. 定義輔助函式計算個別整數的十進位位數和。
2. 運用元組 (Tuple) 作為排序 Key，實現雙層條件的多鍵排序 (Multi-key Sorting)。
3. 使用 while True 配合 try-except 處理 EOF (End-of-File) 串流輸入。
"""

def get_digit_sum(num):
    """計算單一整數的各位數字和 (Sum of digits)。"""
    return sum(int(ch) for ch in str(num))


while True:
    try:
        # 讀取每組資料的第一行：整數個數 N
        n = int(input())

        # 讀取每組資料的第二行：N 個由空白隔開的整數
        nums = list(map(int, input().split()))

        # 多鍵排序：
        # 優先級 1 (Primary Key)：各位數字和 (由小到大)
        # 優先級 2 (Secondary Key)：原始整數數值 (由小到大)
        nums.sort(key=lambda x: (get_digit_sum(x), x))

        # 使用解包運算子 (*) 輸出，自動以空白分隔各數值
        print(*nums)

    except EOFError:
        # 讀取到檔案結尾時安全退出迴圈
        break
