def even_odd(*args):
    command = args[-1]
    nums = args[0:-1]

    if command == "even":
        res = [num for num in nums if num % 2 == 0]
    elif command == "odd":
        res = [num for num in nums if num % 2 != 0]
    return res