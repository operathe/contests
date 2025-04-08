N, M = map(int, input().split())

total_squares = N * N

dangerous_count = 0
dangerous_positions = set()

for _ in range(M):
    a, b = map(int, input().split())
    position = (a, b)

    if position not in dangerous_positions:
        dangerous_positions.add(position)
        dangerous_count += 1

    knight_moves = [
        (2, 1),
        (1, 2),
        (-1, 2),
        (-2, 1),
        (-2, -1),
        (-1, -2),
        (1, -2),
        (2, -1),
    ]

    for da, db in knight_moves:
        na, nb = a + da, b + db
        new_position = (na, nb)
        if 1 <= na <= N and 1 <= nb <= N and new_position not in dangerous_positions:
            dangerous_positions.add(new_position)
            dangerous_count += 1

safe_count = total_squares - dangerous_count

print(safe_count)
