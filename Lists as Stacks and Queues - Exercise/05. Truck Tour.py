from collections import deque

def solve():
    pumps_count = int(input())
    route = deque()

    for i in range(pumps_count):
        petrol, dist_next = map(int, input().split())
        route.append([petrol, dist_next, i])

    counter_stops = 0
    fuel = 0

    while True:
        stop = route[0]
        if stop[0] + fuel - stop[1] >= 0:
            route.append(route.popleft())
            fuel += stop[0] - stop[1]
            counter_stops += 1
            if counter_stops == pumps_count:
                print(route[0][2])
                break
        else:
            route.append(route.popleft())
            counter_stops = 0
            fuel = 0


solve()