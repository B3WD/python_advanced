from collections import deque

cups = deque(map(int, input().split()))
bottles = list(map(int, input().split()))

wasted_water = 0

#main loop
while True:

    if len(cups) == 0:
        print(f"Bottles: {' '.join(map(str, bottles))}")
        break

    if len(bottles) == 0:
        print(f"Cups: {' '.join(map(str, cups))}")
        break

    current_bottle = bottles[-1]
    current_cup = cups[0]

    result = current_cup - current_bottle
    cups[0] = result

    if result <= 0:
        wasted_water += (result * -1)
        cups.popleft()
        bottles.pop()
    else:
        bottles.pop()

print(f"Wasted litters of water: {wasted_water}")