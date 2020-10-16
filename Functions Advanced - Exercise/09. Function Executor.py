def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


def func_executor(*args):
    results = []
    if args:
        for (func, params, *_) in args:
            res = func(*params)
            results.append(res)
        return results