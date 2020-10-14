input_ = input().split("|")[::-1]
num_groups = [group.split() for group in input_]

flattened = []

for group in num_groups:
    [flattened.append(num) for num in group]

print(" ".join(flattened))

# print([item for group in num_groups for item in group])