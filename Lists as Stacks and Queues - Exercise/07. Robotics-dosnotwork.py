from collections import deque

def assembly_line():
    robots = input().split(";")
    start_time = input()
    hours, mins, secs = map(int, start_time.split(":"))
    items = deque()
    time = -1

    #fill the queue with items
    while True:
        item = input()
        if item == "End":
            break
        else:
            items.append(item)

    #set up the bots
    s = []
    is_working = False
    for robot in robots:
        name, work_time = robot.split("-")
        s.append([name, int(work_time), is_working])

    #start the operations
    while True:
        
        if len(items) == 0:
                break

        for i, bot in enumerate(s):

            if len(items) == 0:
                break
            
            time += 1
            secs += 1

            if secs == 60:
                secs = 0
                mins += 1
                if mins == 60:
                    mins = 0
                    hours += 1

            
            if bot[2] == False or time % bot[1] == 0:
                if time % bot[1] == 0:
                    s[i][2] = False
                s[i][2] = True
                print(f"{bot[0]} - {items[0]} [{hours:02}:{mins:02}:{secs:02}]")
                items.popleft()
            else:
                items.append(items.popleft())

            
assembly_line()