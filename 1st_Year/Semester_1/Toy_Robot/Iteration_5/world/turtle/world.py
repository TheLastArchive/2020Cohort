import turtle
# from robot import obstacles

Jeff = turtle.Turtle()
Jeff.color("red")
Jeff._tracer(0, 0)     #This sets up the grid
Jeff.left(90)
Jeff.penup()
Jeff.forward(200)
Jeff.pendown()
Jeff.left(90)
Jeff.forward(100)
Jeff.left(90)
Jeff.forward(400)
Jeff.left(90)
Jeff.forward(200)
Jeff.left(90)
Jeff.forward(400)
Jeff.left(90)
Jeff.forward(100)
Jeff.right(90)
Jeff.penup()
Jeff.back(200)
Jeff.pendown()
Jeff.speed(1)
Jeff._tracer(1, 1)


def safe_zone(robot_data):

    print("{}: Sorry, I cannot go outside my safe zone.".format(robot_data['name']))


def move_forward(robot_data, magnitude, silence):
    """Moves the robot in forward, silence is rated on a scale of 0 - 2 where 0 is not silent and prints all
    output and 2 is complete silence where no output is printed"""

    Jeff.penup()
    if track_position(robot_data, magnitude): Jeff.forward(int(magnitude))

    return robot_data


def move_back(robot_data, magnitude, silence):
    """Moves the robot backwards"""

    Jeff.penup()
    if track_position(robot_data, int(magnitude) * -1): Jeff.back(int(magnitude))
    
    return robot_data


def turn_left(robot_data, silence):

    compass = robot_data.get('compass')
    compass.insert(0, compass[3])  #If the robot is facing North(1 in the list) and turns left,
    compass.pop(4)
    Jeff.left(90)
    return robot_data


def turn_right(robot_data, silence):

    compass = robot_data.get('compass')
    compass.append(compass[0])     #Shifts the entire list backwards.
    compass.pop(0)
    Jeff.right(90)
    return robot_data


def sprint(robot_data, magnitude, silence):

    if magnitude == 0:
        return robot_data
    else:
        robot_data = move_forward(robot_data, magnitude, silence + 1)
        robot_data = sprint(robot_data, int(magnitude) - 1, silence)
        return robot_data


def track_position(robot_data, magnitude):
    """Calculates and keeps track of the robots position"""

    from robot import obstacles

    compass = robot_data['compass']
    temp_x = robot_data.get('x')  #stores the initial position
    temp_y = robot_data.get('y')

    if compass[0] % 2 == 1:   #Checks if the direction is 'odd' (along the y-axis)
        robot_data['y'] += int((compass[0] * magnitude))

        if obstacles.is_position_blocked(robot_data['x'], robot_data['y']) == True or\
            obstacles.is_path_blocked(temp_x, temp_y, robot_data['x'], robot_data['y']) == True:   #path checks
                robot_data['y'] -= int(compass[0] * magnitude)
                print(f"> {robot_data['name']}: Sorry, there is an obstacle in the way.")
                return False

        if abs(robot_data['y']) > 200:  #checking if the robot has gone out of bounds
            safe_zone(robot_data)
            robot_data['y'] -= int((compass[0] * magnitude))
            return False
    else:
        robot_data['x'] += int(((compass[0] / 2)  * magnitude))

        if obstacles.is_position_blocked(robot_data['x'], robot_data['y']) == True or\
            obstacles.is_path_blocked(temp_x, temp_y, robot_data['x'], robot_data['y']) == True:
                robot_data['x'] -= (int((compass[0] / 2))  * magnitude)
                print(f"> {robot_data['name']}: Sorry, there is an obstacle in the way.")
                return False

        if abs(robot_data['x']) > 100:
            safe_zone(robot_data)
            robot_data['x'] -= (int((compass[0] / 2))  * magnitude)
            return False

    return robot_data


def replay_output(robot_data, commands, count):

    reversePrint = ""
    silencePrint = ""

    if commands['reversed'] > 0:
        reversePrint = " in reverse"
    
    if commands['silent'] > 0:
        silencePrint = " silently"

    print(f" > {robot_data['name']} replayed " + str(count) + " commands" + reversePrint + silencePrint + ".")


def display_obstacles(obstacle_list):
    """Uses the turtle to draw the obstacles onto the grid"""

    Jeff._tracer(0, 0)
    Jeff.penup()
    for i in obstacle_list:
        Jeff.goto(i[0], i[1])
        Jeff.pendown()
        Jeff.begin_fill()
        Jeff.goto(i[0], i[1] + 4)
        Jeff.goto(i[0] + 4, i[1] + 4)
        Jeff.goto(i[0] + 4, i[1])
        Jeff.goto(i[0], i[1])
        Jeff.end_fill()
        Jeff.penup()
    Jeff.penup()
    Jeff.goto(0,0)
    Jeff._tracer(1, 1)


def display_obstacles_2(obstacle_list):
    """used if obstacle tuples only have 2 coords, used for mazes instead of obstacles"""
    count = 1
    Jeff._tracer(0, 0)
    Jeff.penup
    for i in obstacle_list:
        Jeff.goto(i[0], i[1])
        Jeff.pendown
        try: j = obstacle_list[count]
        except IndexError: return
        Jeff.goto(j[0], j[1])
        count += 1
    Jeff.penup()
    Jeff.goto(0,0)
    Jeff._tracer(1, 1)


def draw_path(maze_path):

    Jeff.penup
    for i in maze_path:
        Jeff.goto(i[0], i[1])
        Jeff.pendown
    Jeff.penup
    Jeff.goto(0, 0)