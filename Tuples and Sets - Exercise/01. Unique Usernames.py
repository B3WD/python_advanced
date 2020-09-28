names_count = int(input())

unique_names = set([input() for _ in range(names_count)])
print("\n".join(unique_names))