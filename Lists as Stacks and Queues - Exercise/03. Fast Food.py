from collections import deque


def solve():

    food_q = int(input())
    orders = deque(map(int, input().split()))

    print(max(orders))
    while True:

        if orders[0] <= food_q:
            food_q -= orders.popleft()
            if len(orders) == 0:
                print("Orders complete")
                break
        else:
            print(f"Orders left: {' '.join(map(str, orders))}")
            break


solve()