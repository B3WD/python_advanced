from collections import deque


def set_robot_states(robots, state=0):
    robot_state_dict = dict()

    for robot in robots:
        robot_state_dict[robot] = 0

    return robot_state_dict

def set_robot_timers(robots, time=0):
    robot_timers = dict()

    for robot in robots:
        robot_timers[robot] = robots[robot]

    return robot_timers

def unpackRobots(robots):
    robots_dict = dict()
    for robot_time in robots.split(';'):
        robot_name, robot_time = robot_time.split('-')
        robots_dict[robot_name] = int(robot_time)

    return robots_dict

def tickDownWorkingBots(robots_states, robots_timers):
    for robot in robots_states:
        if robots_states[robot]:
            robots_timers[robot] -= 1

def resetBots(robots_states, robots_timers, robots):
    for robot in robots.keys():
        if robots_timers[robot] <= 0:
            robots_states[robot] = 0
            robots_timers[robot] = robots[robot]

def unpackTime(time):
    h, m, s = time.split(':')
    return int(h), int(m), int(s)

def tickTime(h, m, s):
    s += 1
    if(s > 59):
        s = 0
        m += 1
        if( m > 59):
            m = 0
            h += 1
            if(h > 23):
                h = 0

    return h, m, s

def printTime(h, m, s):
    return f"{h:02}:{m:02}:{s:02}"

def factory(robots:dict, elems:deque, time):
    robot_state_dict = set_robot_states(robots.keys())
    robot_timers = set_robot_timers(robots)
    h, m, s = unpackTime(time)

    while(True):

        atlestOneFree = False
        for robot in robots:

            if(len(elems)==0):
                return 0

            if robot_state_dict[robot] == 0:
                robot_state_dict[robot] = 1
                atlestOneFree = True
                elem = elems.popleft()

                tickDownWorkingBots(robot_state_dict, robot_timers)
                h, m, s = tickTime(h, m, s)
                resetBots(robot_state_dict, robot_timers, robots)

                print(f"{robot} - {elem} [{printTime(h, m, s)}]")

        if not atlestOneFree:
            tickDownWorkingBots(robot_state_dict, robot_timers)
            elems.rotate(-1)
            h, m, s = tickTime(h, m, s)
            resetBots(robot_state_dict, robot_timers, robots)
        

def getElems():
    elemQ = deque()

    while(True):
        elem = input()

        if(elem == "End"):
            break
        
        elemQ.append(elem)

    return elemQ


robots_dict = unpackRobots(input())
start_time = input()
elem_q = getElems()

factory(robots_dict, elem_q, start_time)