def solve(chems):
    chems = set(" ".join(chems).split())
    print("\n".join(chems))

count = int(input())

chems = [input() for _ in range(count)]

solve(chems)