from collections import deque


def set_robot_states(robots, state=0):
    robot_state_dict = dict()

    for robot in robots:
        robot_state_dict[robot] = 0

    return robot_state_dict


def set_robot_start_time(robots, time=0):
    robot_start_time = dict()

    for robot in robots:
        robot_start_time[robot] = 0

    return robot_start_time


def factory(robots:dict, elems:deque, time):
    robot_state_dict = set_robot_states(robots.keys())
    robot_start_time = set_robot_start_time(robots.keys())

    time += 1
    while(True):

        for robot, state in robot_state_dict.items():

            if len(elems) == 0:
                break

            if state == 0:
                elem = elems.popleft()
                robot_state_dict[robot] = 1
                robot_start_time[robot] = time
                print(f"{robot} - {elem} [{time}]")
                time += 1

            for robot, rtime in robots.items():
                if (time - robot_start_time[robot]) % rtime == 0:
                    robot_state_dict[robot] = 0

        elems.rotate(-1)
        time += 1

def unpackRobots(robots):
    robots_dict = dict()
    for robot_time in robots.split(';'):
        robot_name, robot_time = robot_time.split('-')
        robots_dict[robot_name] = int(robot_time)

    return robots_dict


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
start_time = 0
elem_q = getElems()

factory(robots_dict, elem_q, start_time)