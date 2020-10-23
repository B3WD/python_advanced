from collections import deque


def solve(customers, taxis):
    
    total_ride_time = 0

    while True:

        if not customers:
            print("All customers were driven to their destinations")
            print(f"Total time: {total_ride_time} minutes")
            break

        if not taxis:
            print("Not all customers were driven to their destinations")
            print(f"Customers left: {', '.join(map(str, customers))}")
            break

        curr_customer = customers[0]
        curr_taxi = taxis[-1]

        if curr_customer <= curr_taxi:
            total_ride_time += curr_customer
            customers.popleft()
            taxis.pop()
        else:
            taxis.pop()


customers = deque([int(x) for x in input().split(", ")])
taxis = [int(x) for x in input().split(", ")]

solve(customers, taxis)