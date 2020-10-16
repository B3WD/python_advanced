def get_odd_sum(arr):
    return sum([x for x in arr if x % 2 != 0])


def get_even_sum(arr):
    return sum([x for x in arr if x % 2 == 0])


def solve(command):
    if command == "Odd":
        res = get_odd_sum(nums)
    elif command == "Even":
        res = get_even_sum(nums)

    res *= len(nums)

    print(res)


command = input()

nums = [int(x) for x in input().split()]

solve(command)