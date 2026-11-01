# 1. 建立複數類別與運算子多載
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        new_real = self.real * other.real - self.imag * other.imag
        new_imag = self.real * other.imag + other.real * self.imag
        return Complex(new_real, new_imag)

# 2. 讀取運算筆數
n = int(input())

# 3. 依序處理每一筆運算
for i in range(n):
    data = input().split()
    op = data[0]
    a = int(data[1])
    b = int(data[2])
    c = int(data[3])
    d = int(data[4])

    c1 = Complex(a, b)
    c2 = Complex(c, d)

    if op == '+':
        ans = c1 + c2
    elif op == '-':
        ans = c1 - c2
    elif op == '*':
        ans = c1 * c2

    # 4. 輸出結果
    print(ans.real, ans.imag)