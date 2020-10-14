total_items = 0
total_quality = 0

#      count, q
inv = {category:[] for category in input().split(", ")}

lines_count = int(input())


for _ in range(lines_count):

    category, item, other = input().split(" - ")

    count_info, quality_info = other.split(";")

    count = int(count_info.split(":")[1])

    quality = int(quality_info.split(":")[1])

    if item not in inv[category]:
        inv[category].append(item)
        total_items += count
        total_quality += quality

print(f"Count of items: {total_items}")
print(f"Average quality: {total_quality / len(inv):.2f}")

for (category, items) in inv.items():
    print(f"{category} -> {', '.join(items)}")
