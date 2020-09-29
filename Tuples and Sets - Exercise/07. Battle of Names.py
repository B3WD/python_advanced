def solve(liens):
    results_odd = set()
    results_even = set()
    for i, name in enumerate(lines):
        ascii_sum = 0
        for char in name:
            ascii_sum += ord(char)
        result = int(ascii_sum / (i + 1))
        if result % 2 != 0:
            results_odd.add(result)
        else:
            results_even.add(result)
    
    if sum(results_odd) == sum(results_even):
        print(", ".join(map(str, results_odd | results_even)))

    elif sum(results_odd) > sum(results_even):
        print(", ".join(map(str, results_odd - results_even)))

    elif sum(results_odd) < sum(results_even):
        print(", ".join(map(str, results_odd ^ results_even)))


lines_count = int(input())

lines = [input() for _ in range(lines_count)]

solve(lines)