N = input()

# if N.count("1") == 1 and N.count("2") == 2 and N.count("3") == 3:
#     print("Yes")
# else:
# print("No")

N = "".join(sorted(N))

print("Yes" if N == "122333" else "No")
