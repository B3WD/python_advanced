nums = [int(x) for x in input().split()]

neg_sum = 0
pos_sum = 0

for num in nums:
    if num > 0:
        pos_sum += num
    else:
        neg_sum += num

print(neg_sum)
print(pos_sum)

if pos_sum > abs(neg_sum):
    print(f"The positives are stronger than the negatives")
else:
    print(f"The negatives are stronger than the positives")