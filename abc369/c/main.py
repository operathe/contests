# 入力を受け取る
n = int(input())
A = list(map(int, input().split()))

# 隣接する要素の差分を前計算
diffs = [A[i + 1] - A[i] for i in range(n - 1)]

# 答えの初期値は数列の長さ（長さ1の部分列の数）
ans = n

# 差分配列を使って等差数列を探索
i = 0
while i < n - 1:
    # 現在の差分値
    curr_diff = diffs[i]

    # 同じ差分が連続する長さを計算
    length = 1
    while i + length < n - 1 and diffs[i + length] == curr_diff:
        length += 1

    # 長さlength+1の等差数列から作れる部分列の数を加算
    # (k * (k-1)) // 2 where k = length + 1
    k = length + 1
    ans += k * (k - 1) // 2

    # 次の位置へジャンプ
    i += length

print(ans)
