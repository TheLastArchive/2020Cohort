from collections import defaultdict
import timeit
from world.turtle.world import draw_path

obstacle_list = []

def solve(robot_data, command, obstacle_list_robot):
    """Uses a 'Breadth-First Search algorithim' to solve the maze"""

    global obstacle_list
    obstacle_list = list(obstacle_list_robot)
    index = 1
    command = command.split(" ")
    if 'top' in command:
        exit = (0, 200)
    elif 'bottom' in command:
        exit = (0, -200)
    elif 'left' in command:
        exit = (-100, 0)
        index = 0
    elif 'right' in command:
        exit = (100, 0)
        index = 0
    else:
        exit = (0, 200)
        command.append('top')
        

    edges = get_edges()
    connected_edges = connect_the_edges(edges)

    #Begin the BFS
    queue = [[(0, 0)]] #Origin
    paths = []
    #print(exit)
    while len(queue) > 0: 
        path = queue.pop(0) 
        node = path[-1] 
        if node not in paths: 
            neighbours = connected_edges[node] 
            for neighbour in neighbours: 
                new_path = list(path) 
                new_path.append(neighbour) 
                queue.append(new_path) 
                if neighbour[index] == exit[index]: 
                    print(f"{robot_data['name']}: I am at the {command[1]} edge")
                    draw_path(new_path)
                    return True
            paths.append(node) 
    print("error")
    return False


def get_edges():
    """Runs through the maze point by point and tracks every possible position"""

    edges = []
    #Start search at the bottom left corner of the maze and move to the top right
    for y in range(-200, 201):
        for x in range(-100, 101):
            if not is_position_blocked(x, y): #False == No Obstacles
                #If y == 200, y + 1 will be out of bounds. Don't want.
                if y != 200 and not is_position_blocked(x, y + 1): #Check cell above
                    edges.append(((x, y), (x, y + 1)))
                if x != 100 and not is_position_blocked(x + 1, y): #Check cell to the right
                    edges.append(((x,y), (x + 1, y)))
    
    return edges


def connect_the_edges(edges):
    """Iterates through the possible positions and connects the edges"""
    #Using defaultdict to avoid hundreds of thousands of try/excepts to bypass the
    #hundreds of thousands of KeyErrors
    connected_edges = defaultdict(list)
    for edge in edges:
        temp1 = edge[0]
        temp2 = edge[1]
        connected_edges[temp1].append(temp2)
        connected_edges[temp2].append(temp1)
    
    # for edge in connected_edges:
    #     print(edge)
    return connected_edges


def is_position_blocked(x, y):
    """Checks if the position is blocked by an obstacle
    Copied over from obstacles / alex_maze for speed sake
    That's a lie, imports are scary"""

    for i in obstacle_list:
        if (i[0] <= x <= i[0] + 4) and\
            (i[1] <= y <= i[1] + 4): return True
    
    return False


# if __name__ == '__main__':

#     print(timeit.timeit(solve, number=1))


"""Links that make me happy :)

'Maze Solving - Computerphile from Computerphile'
https://www.youtube.com/watch?v=rop0W4QDOUI&ab_channel=Computerphile

Python Path Finding Tutorial - Breadth First Search Algorithm from Tech With Tim
https://www.youtube.com/watch?v=hettiSrJjM4&t=101s&ab_channel=TechWithTim

Breadth-First Search from Wikipedia 
https://en.wikipedia.org/wiki/Breadth-first_search

Python Breadth First Search Maze solving program from Davis MT
https://www.youtube.com/watch?v=ZuHW4fS60pc&ab_channel=DavisMT"""

