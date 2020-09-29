import turtle

Jeff = turtle.Turtle()
Jeff.color("red")
Jeff.speed(11)     #This sets up the grid
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


def safe_zone(robot_data):

    print("{}: Sorry, I cannot go outside my safe zone.".format(robot_data['name']))


def move_forward(robot_data, magnitude, silence):
    """Moves the robot in forward, silence is rated on a scale of 0 - 2 where 0 is not silent and prints all
    output and 2 is complete silence where no output is printed"""

    if track_position(robot_data, magnitude): Jeff.forward(int(magnitude))

    return robot_data


def move_back(robot_data, magnitude, silence):
    """Moves the robot backwards"""

    if track_position(robot_data, magnitude * -1): Jeff.back(int(magnitude))
    
    return robot_data


def turn_left(robot_data, silence):

    Jeff.left(90)
    return robot_data


def turn_right(robot_data, silence):

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

    compass = robot_data['compass']

    if compass[0] % 2 == 1:   #Checks if the direction is 'odd' (along the y-axis)
        robot_data['y'] += (compass[0] * magnitude)
        if abs(robot_data['y']) > 200:
            safe_zone(robot_data)
            robot_data['y'] -= (compass[0] * magnitude)
            return False
    else:
        robot_data['x'] += (int((compass[0] / 2))  * magnitude)
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

