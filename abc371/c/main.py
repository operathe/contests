from itertools import permutations


def create_edge_set(edges):
    edge_set = set()
    for u, v in edges:
        edge_set.add((u - 1, v - 1))
        edge_set.add((v - 1, u - 1))
    return edge_set


def main():
    n = int(input())

    mg = int(input())
    uv = [tuple(map(int, input().split())) for _ in range(mg)]

    mh = int(input())
    ab = [tuple(map(int, input().split())) for _ in range(mh)]

    a = [[0] * n for _ in range(n)]
    for i in range(n - 1):
        row = list(map(int, input().split()))
        for j, value in enumerate(row):
            a[i][i + j + 1] = value
            a[i + j + 1][i] = value

    edges_g = create_edge_set(uv)
    edges_h = create_edge_set(ab)

    ans = float("inf")

    for perm in permutations(range(n)):
        sum = 0
        for i in range(n):
            for j in range(i):
                if ((i, j) in edges_h) != ((perm[i], perm[j]) in edges_g):
                    sum += a[i][j]
        ans = min(ans, sum)

    print(ans)


if __name__ == "__main__":
    main()
