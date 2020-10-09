import random

obstacle_list = []

def create_obstacles():
    """You'll never guess what this function does"""

    global obstacle_list
    num_of_obstacles = random.randint(0, 9)    #Generates how many obstacles will be created
    while num_of_obstacles > 0:
        x1 = random.randint(-100, 101)
        y1 = random.randint(-200, 201)
        x2 = x1 + 4
        y2 = y1 + 4
        tup = tuple([x1, y1, x2, y2])   #It's a tuple because ____
        obstacle_list.append(tup)
        num_of_obstacles -= 1

    return obstacle_list

def is_position_blocked(x, y):
    """Checks if the position is blocked by an obstacle"""

    for i in obstacle_list:
        if (i[0] <= x <= i[2]) and\
            (i[1] <= y <= i[3]): return True
        else: pass
    
    return False


def is_path_blocked(x1, y1, x2, y2):
    """Checks if the path is blocked by an obstacle"""

    if x1 > x2:
        temp = x1
        x1 = x2
        x2 = temp
    if y1 > y2:
        temp = y1
        y1 = y2
        y2 = temp

    for i in obstacle_list:
        if (i[0] in range(x1, x2 + 1) or i[2] in range(x1, x2 + 1)):
            if (i[1] <= y1 <= i[3]): return True
        if (i[1] in range(y1, y2 + 1) or i[3] in range(y1, y2 + 1)):
            if (i[0] <= x1 <= i[2]): return True

    return False


def get_obstacles():

    #print(obstacle_list)
    return obstacle_list


def reset_obstacles():

    global obstacle_list
    obstacle_list = []

create_obstacles()