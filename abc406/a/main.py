a, b, c, d = map(int, input().split())

if c < a or (c == a and d <= b):
    print("Yes")
else:
    print("No")
