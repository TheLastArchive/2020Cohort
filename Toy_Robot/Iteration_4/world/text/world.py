
def safe_zone(robot_data):

    print("{}: Sorry, I cannot go outside my safe zone.".format(robot_data['name']))


def move_forward(robot_data, magnitude, silence):
    """Moves the robot in forward, silence is rated on a scale of 0 - 2 where 0 is not silent and prints all
    output and 2 is complete silence where no output is printed"""

    if track_position(robot_data, int(magnitude)) != False and silence < 2:
        print(" > {} moved forward by {} steps.".format(robot_data['name'], magnitude))
    if silence < 1:
        print(" > {} now at position ({},{}).".format(robot_data['name'], robot_data['x'], robot_data['y']))

    return robot_data


def move_back(robot_data, magnitude, silence):
    """Moves the robot backwards"""

    if track_position(robot_data, int(magnitude) * -1) != False and silence < 2:        #Negative magnitude to show backwards movement
        print(" > {} moved back by {} steps.".format(robot_data['name'], magnitude))
        print(" > {} now at position ({},{}).".format(robot_data['name'], robot_data['x'], robot_data['y']))

    return robot_data


def turn_left(robot_data, silence):

    compass = robot_data.get('compass')
    compass.insert(0, compass[3])  #If the robot is facing North(1 in the list) and turns left,
    compass.pop(4)                 #he will then be facing East (-2 in the list) so essentially shifting the entire list forward 
                                   #whenever the robot turns left.
    if silence < 2:
        print (" > {} turned left." .format(robot_data['name']))
        print(" > {} now at position ({},{}).".format(robot_data['name'], robot_data['x'], robot_data['y']))
    
    robot_data['compass'] = compass
    return robot_data


def turn_right(robot_data, silence):

    compass = robot_data.get('compass')
    compass.append(compass[0])     #Shifts the entire list backwards.
    compass.pop(0)
    if silence < 2:
        print (" > {} turned right." .format(robot_data['name']))
        print(" > {} now at position ({},{}).".format(robot_data['name'], robot_data['x'], robot_data['y']))

    robot_data['compass'] = compass
    return robot_data


def sprint(robot_data, magnitude, silence):

    if magnitude == 0:
        if silence < 2: print(" > {} now at position ({},{}).".format(robot_data['name'], robot_data['x'], robot_data['y']))
        return robot_data
    else:
        robot_data = move_forward(robot_data, magnitude, silence + 1)
        robot_data = sprint(robot_data, magnitude - 1, silence)
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
    print(f" > {robot_data['name']} now at position ({robot_data['x']}, {robot_data['y']}).")