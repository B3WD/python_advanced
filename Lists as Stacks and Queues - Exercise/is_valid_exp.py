def is_valid_expresion(expresion):
    cnt = 0

    for ch in expresion:
        if ch == '(':
            cnt += 1
        elif ch == ')':
            cnt -= 1
        if cnt < 0:
            return False

    return True

print(is_valid_expresion("))(("))
print(is_valid_expresion("(()())"))
print(is_valid_expresion("(()())()())"))