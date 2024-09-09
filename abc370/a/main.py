n = int(input())
# n個の数列が標準入力で与えられる
# 1番目の数列の要素数は１個、2番目の数列の要素数は２個、...、n番目の数列の要素数はn個
# 入力を受けとる
a = [list(map(int, input().split())) for _ in range(n)]
# 各数列を出力して確認
for i in range(n):
    print(f"数列 {i+1}: {a[i]}")
print(a[0][0])
