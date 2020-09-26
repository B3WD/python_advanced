from collections import deque

green_light_time = int(input())
grace_time_period = int(input())

car_queue = deque()
passed_cars = 0
crash = False

while True:

    if crash:
        break

    command = input()

    if command == "END":
        print("Everyone is safe.")
        print(f"{passed_cars} total cars passed the crossroads.")
        break

    elif command == "green":
        current_time = green_light_time
        while len(car_queue) and current_time > 0:
            current_car = car_queue[0]
            if current_time > 0:
                if current_time + grace_time_period - len(current_car) >= 0:
                    #car passes safely
                    car_queue.popleft()
                    passed_cars += 1
                    current_time -= len(current_car)
                else:
                    print("A crash happened!")
                    print(f"{current_car} was hit at {current_car[current_time + grace_time_period]}.")
                    crash = True
                    break
    
    else:
        #add the car
        car_queue.append(command)
