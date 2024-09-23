n, m = map(int, input().split())
taro_exist = [False for _ in range(n)]
for i in range(m):
    a, b = input().split()
    a = int(a) - 1
    if b == "F" or taro_exist[a]:
        print("No")
    else:
        taro_exist[a] = True
        print("Yes")
