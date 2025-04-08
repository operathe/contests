s = input()

# 文字列をソートしてABCと一致するかどうかを判定
if sorted(s) == list("ABC"):
    print("Yes")
else:
    print("No")
