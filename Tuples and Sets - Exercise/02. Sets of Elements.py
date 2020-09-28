def find_unique_and_common(line_1, line_2):
    print("\n".join(map(str, set(line_1) & set(line_2))))


line_1_count, line_2_count = map(int, input().split())

line_1 = [int(input()) for _ in range(line_1_count)]
line_2 = [int(input()) for _ in range(line_2_count)]

find_unique_and_common(line_1, line_2)