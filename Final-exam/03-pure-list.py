from collections import deque


def best_list_pureness(*args):
    nums = deque([int(x) for x in args[0]])
    max_rotations = int(args[-1]) 
    current_purrest = 0

    for i in range(max_rotations + 1):
        res = 0
        for index, num in enumerate(nums):
            res += index * num

        nums.appendleft(nums.pop())

        if res > current_purrest:
            cycles = i
            current_purrest = res

    return f"Best pureness {current_purrest} after {cycles} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
