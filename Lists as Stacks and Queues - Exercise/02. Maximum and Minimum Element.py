def solve():
    s = []
    num_queries = int(input())
    
    for _ in range(num_queries):

        command = input()

        if command.startswith("1"):
            s.append(command.split()[1])

        elif s:
                
            if command.startswith("2"):
                s.pop()

            elif command.startswith("3"):
                print(max(s))

            elif command.startswith("4"):
                print(min(s))

    print(", ".join(reversed(s)))

solve()