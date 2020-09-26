def check_balance(string):
    s = []
    for char in string:
        if char in {"(", "{", "["}:
            s.append(char)
        else:
            if not s:
                s.append("unbalanced")
                break
            elif s[-1] == "(" and char == ")":
                s.pop()
            elif s[-1] == "[" and char == "]":
                s.pop()
            elif s[-1] == "{" and char == "}":
                s.pop()
            else:
                break
    if s:
        print("NO")
    else:
        print("YES")

parantheses = input()

check_balance(parantheses)