def solve(lines):
    longest_intersec = []
    for line in lines:
        (r1, r2) = line.split("-")
        (r1_start, r1_end) = map(int, r1.split(","))
        (r2_start, r2_end) = map(int, r2.split(","))
        current_longest_intersec = set(range(r1_start, r1_end + 1)) & set(range(r2_start, r2_end + 1))
        if len(current_longest_intersec) > len(longest_intersec):
            longest_intersec = current_longest_intersec
    
    print(f"Longest intersection is {sorted(longest_intersec)} with length {len(longest_intersec)}")


num_lines = int(input())

lines = [input() for _ in range(num_lines)]

solve(lines)