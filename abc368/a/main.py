# 入力を受け取る
N, K = map(int, input().split())
A = list(map(int, input().split()))

# リストのスライスを使って、リストの後ろK個と前N-K個を取り出して結合する
B = A[-K:] + A[:-K]

# 結果を出力する
print(*B)
