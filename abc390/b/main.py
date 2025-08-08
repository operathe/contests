import sys


def is_geometric(seq):
    n = len(seq)
    if n <= 2:
        return True
    for i in range(n - 2):
        if seq[i] * seq[i + 2] != seq[i + 1] * seq[i + 1]:
            return False
    return True


def main():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    a = data[1:]
    print("Yes" if is_geometric(a) else "No")


if __name__ == "__main__":
    main()
