# 1. 讀取輸入字串與位移步數 k
text = input()
k = int(input())
ans = ""

# 2. 逐字判斷並依照類別進行循環位移
for ch in text:
    if ch.isupper():
        new_ch = chr((ord(ch) - ord('A') + k) % 26 + ord('A'))
        ans += new_ch
    elif ch.islower():
        new_ch = chr((ord(ch) - ord('a') + k) % 26 + ord('a'))
        ans += new_ch
    elif ch.isdigit():
        new_ch = chr((ord(ch) - ord('0') + k) % 10 + ord('0'))
        ans += new_ch
    else:
        ans += ch

# 3. 輸出加密後的完整句子
print(ans)