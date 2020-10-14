words = input().split(", ")

res = [f"{word} -> {len(word)}" for word in words]

print(", ".join(res))