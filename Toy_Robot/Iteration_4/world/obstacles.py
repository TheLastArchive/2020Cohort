import random

obstacle_list = []
num_of_obstacles = random.randint(0, 9)

while num_of_obstacles > -1:
    x1 = random.randint(-100, 101)
    y1 = random.randint(-200, 201)
    x2 = x1 + 4
    y2 = y1 + 4
    tup = tuple([x1, y1, x2, y2])
    obstacle_list.append(tup)
    num_of_obstacles -= 1
    

def is_position_blocked(x, y):

    for i in obstacle_list:
        if (i[0] <= x >= i[2]) and\
            (i[1] <= y >= i[3]): return True
        else: pass
    
    return False


def is_path_blocked(x1, y1, x2, y2):

    for i in obstacle_list:
        if i[0] in range(x1, x2 + 1):
            if i[1] in range(y1, y2 + 1): return True
        else: pass
    
    return False

def get_obstacles():

    print(obstacle_list)
    return obstacle_list

get_obstacles()