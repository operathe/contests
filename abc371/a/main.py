s = input().split()

if s[0] != s[1]:
    print("A")
elif s[0] == s[2]:
    print("B")
else:
    print("C")


AB, AC, BC = input().split()
if AB == "<" and AC == ">" or AB == ">" and AC == "<":
    print("A")
elif AB == "<" and BC == "<" or AB == ">" and BC == ">":
    print("B")
else:
    print("C")
