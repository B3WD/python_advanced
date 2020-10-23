#Needs rewriting, and splitting into funcs

from collections import deque


# def create_bomb(material_sum, target):
#     if material_sum == target:
#         if target == 40:
#             detura_b += 1
#         if target == 60:
#             cherry_b += 1
#         if target == 120:
#             smoke_b += 1
#         bombs.popleft()


bombs = deque([int(x) for x in input().split(", ")])
casings = [int(x) for x in input().split(", ")]

detura_b = 0
cherry_b = 0
smoke_b = 0


while True:

    current_bomb = bombs[0]
    current_casing = casings[-1]
    sum_b_c =  current_bomb + current_casing

    if sum_b_c == 40:
        detura_b += 1
        bombs.popleft()
        casings.pop()

    elif sum_b_c == 60:
        cherry_b += 1
        bombs.popleft()
        casings.pop()

    elif sum_b_c == 120:
        smoke_b += 1
        bombs.popleft()
        casings.pop()

    else:
        casings[-1] -= 5

    if not bombs or not casings:
        print("You don't have enough materials to fill the bomb pouch.")
        break

    if detura_b >= 3 and cherry_b >= 3 and smoke_b >= 3:
        print("Bene! You have successfully filled the bomb pouch!")
        break

if bombs:   
    print(f"Bomb Effects: {', '.join(map(str, bombs))}")
else:
    print(f"Bomb Effects: empty")

if casings:   
    print(f"Bomb Casings: {', '.join(map(str, casings))}")
else:
    print(f"Bomb Casings: empty")

print(f"Cherry Bombs: {cherry_b}")
print(f"Datura Bombs: {detura_b}")
print(f"Smoke Decoy Bombs: {smoke_b}")