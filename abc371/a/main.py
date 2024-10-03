AB, AC, BC = input().split()
if AB == "<" and AC == ">" or AB == ">" and AC == "<":
    print("A")
elif AB == "<" and BC == "<" or AB == ">" and BC == ">":
    print("B")
else:
    print("C")
