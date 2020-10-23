def numbers_searching(*nums):
    nums = [int(x) for x in list(nums)]
    non_unique_nums = sorted(list({x for x in nums if nums.count(x) > 1}))
    unique_nums = set(nums)

    i = 1
    while True:
        missing_num = min(unique_nums) + i
        if missing_num in unique_nums:
            i += 1
            continue
        else:
            break

    return [missing_num, non_unique_nums]