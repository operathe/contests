def solve(a, b, c):
    if b < c:
        return a < b or c < a
    else:
        return a < b and c < a


a, b, c = map(int, input().split())
print("Yes" if solve(a, b, c) else "No")
