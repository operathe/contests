az = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
S = input()
ans = 0

if not all(char in S for char in az):
    raise ValueError("S must contain all alphabets")

indices = [S.index(char) for char in az]

for i in range(25):
    ans += abs(S.index(az[i + 1]) - S.index(az[i]))
print(ans)
