
def simulate_rope(motions):
    positions = set()  # Set to store visited positions
    x, y = 0, 0  # Initial position of head and tail

    for motion in motions:
        direction = motion[0]
        steps = int(motion[1:])

        for _ in range(steps):
            if direction == 'R':
                x += 1
            elif direction == 'L':
                x -= 1
            elif direction == 'U':
                y -= 1
            elif direction == 'D':
                y += 1

            # Update tail position if necessary
            if abs(x - y) == 2:
                tail_x = x if x == y else x + 1 if x > y else x - 1
                tail_y = y if x == y else y + 1 if y > x else y - 1
                positions.add((tail_x, tail_y))

            positions.add((x, y))  # Add current position to visited positions

    return len(positions)  # Return the count of unique visited positions


# Example input
motions = [
    'R4',
    'U4',
    'L3',
    'D1',
    'R4',
    'D1',
    'L5',
    'R2'
]

result = simulate_rope(motions)
print(f"The tail of the rope visits {result} positions at least once.")
