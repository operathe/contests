def count_pairs(n, m, a):
    cumsum = [0] * (2 * n + 1)
    for i in range(2 * n):
        cumsum[i + 1] = (cumsum[i] + a[i % n]) % m

    count = [0] * m
    result = 0

    for i in range(n):
        count[cumsum[i]] += 1

    for i in range(n):
        result += count[cumsum[i + n]]
        if cumsum[i + n] == cumsum[i]:
            result -= 1  # 自分自身とのペアを除外
        count[cumsum[i]] -= 1
        count[cumsum[i + n]] += 1

    return result


def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    result = count_pairs(n, m, a)
    print(result)


if __name__ == "__main__":
    main()
