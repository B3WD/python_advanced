def solve():
    clothes = list(map(int, input().split()))
    max_rack_capacity = int(input())

    num_racks = 0
    current_rack_cap = 0

    while clothes:

        if current_rack_cap + clothes[-1] <= max_rack_capacity:
            if len(clothes) == 1:
                num_racks += 1
            current_rack_cap += clothes.pop()
        else:
            num_racks += 1
            current_rack_cap = 0

    print(num_racks)

solve()