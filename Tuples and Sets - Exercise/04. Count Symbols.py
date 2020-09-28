def solve(word):
    chars = dict()
    for char in word:
        if char not in chars:
            chars[char] = 0
        chars[char] += 1
        
    for (key, value) in sorted(chars.items()):
        print(f"{key}: {value} time/s")


solve(input())