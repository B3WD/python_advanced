def solve(line):
    numbers_for_ops = []
    ops = ["*", "+", "-", "/"]
    for item in line:
        if item in ops:
            operator = item
            if operator == "*":
                res = 1
                for num in numbers_for_ops:
                    res *= num
                numbers_for_ops = [res]

            elif operator == "+":
                res = 0
                for num in numbers_for_ops:
                    res += num
                numbers_for_ops = [res]

            elif operator == "-":
                res = numbers_for_ops[0]
                for num in numbers_for_ops[1:]:
                    res -= num
                numbers_for_ops = [res]

            elif operator == "/":
                res = numbers_for_ops[0]
                for num in numbers_for_ops[1:]:
                    res /= num
                numbers_for_ops = [int(res)]
                    
        else:
            numbers_for_ops.append(int(item))

    return numbers_for_ops[0]

line =  input().split()

res = solve(line)

print(res)