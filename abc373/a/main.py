# N = 12
#
# ans = 0
#
# for i in range(1, N + 1):
#     S = input()
#     if len(S) == i:
#         ans += 1
#
# print(ans)
ans = sum(len(input()) == i for i in range(1, 13))
print(ans)


