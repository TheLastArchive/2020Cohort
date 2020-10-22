import random
from world.turtle import world


obstacle_list = []

def hard_code_maze():
    """This maze is hardcoded"""
    
    global obstacle_list 
    obstacle_list = [[-10, -5, -6, -5], [-10, 30, -6, 30], [-20, 30, -16, 30],
                    [-20, -45, -16, -45], [30, -45, 34, -45]]
    
    world.create_maze(obstacle_list)
    pass

def create_obstacles():
    """Randomly generates a large amount of obstacles"""

    global obstacle_list
    for i in range(150):
        x1 = random.randint(-100, 101)
        while x1 in range(-10, 10):
            x1 = random.randint(-100, 101)
        y1 = random.randint(-200, 201)
        while y1 in range(-10, 10):
            y1 = random.randint(-200, 201)
        x2 = x1 + 4
        y2 = y1 + 4
        tup = tuple([x1, y1, x2, y2])   #It's a tuple because ____
        obstacle_list.append(tup)

    return obstacle_list
    #world.display_obstacles(obstacle_list)


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

lots_of_obstacles()