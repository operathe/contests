x = input()

while x.endswith("0"):
    x = x[:-1]
    if x.endswith("."):
        x = x[:-1]
        break
print(x)
