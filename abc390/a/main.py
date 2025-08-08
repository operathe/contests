import sys

def can_sort_by_one_adjacent_swap(a):
    n = len(a)
    for i in range(n - 1):
        b = a.copy()
        b[i], b[i + 1] = b[i + 1], b[i]
        if all(b[j] == j + 1 for j in range(n)):
            return True
    return False

def main():
    a = list(map(int, sys.stdin.read().split()))
    print("Yes" if can_sort_by_one_adjacent_swap(a) else "No")

if __name__ == "__main__":
    main()
