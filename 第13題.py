# 1. 定義花色權重（黑桃 > 紅心 > 方塊 > 梅花）
suit_order = {'S': 4, 'H': 3, 'D': 2, 'C': 1}

# 2. 定義排序鍵值函式：回傳 (花色權重, 點數值)
def card_key(card):
    return suit_order[card[0]], int(card[1:])

# 3. 讀取總疊數 n，逐疊進行排序與輸出
n = int(input())
for i in range(n):
    cards = input().split()
    cards.sort(key=card_key, reverse=True)
    print(*cards)