nums = list(map(int, input().split(", ")))

pos = [num for num in nums if num >= 0]
neg = [num for num in nums if num < 0]
even = [num for num in nums if num % 2 == 0]
odd = [num for num in nums if num % 2 != 0]

print(f"Positive: {', '.join(map(str, pos))}")
print(f"Negative: {', '.join(map(str, neg))}")
print(f"Even: {', '.join(map(str, even))}")
print(f"Odd: {', '.join(map(str, odd))}")