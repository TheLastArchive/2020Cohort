import re

def robot_start():
    """This is the entry function, do not change"""

    robot_data = {'name': "", 'x': 0, 'y': 0, 'compass': [1, 2, -1, -2], 'power': True, 'movements': []}

    robot_data['name'] = name_robot()
    check_command(robot_data)
    pass

def name_robot():
    """Names the robot"""

    name = input("What do you want to name your robot? ")
    print("{}: Hello kiddo!".format(name))

    return name


def error(robot_data, command):
    """Displays an error message upon an invalid command"""
    print("{}: Sorry, I did not understand '{}'.".format(robot_data['name'], command))


def shut_down(robot_data, ignore_me):
    """Ends the robot's agonising turmoil"""
    

    print("{}: Shutting down..".format(robot_data['name']))
    robot_data['power'] = False

    return robot_data

def safe_zone(robot_data):

    print("{}: Sorry, I cannot go outside my safe zone.".format(robot_data['name']))
    

def help_command(robot_data, ignore_me):
    """"I'm helping"""
    commands = [
        "OFF  - Shut down robot",
        "HELP - provide information about commands",
        "FORWARD*  - Moves forwards",
        "BACKWARD* - Moves backwards",
        "RIGHT    - Turns right",
        "LEFT     - Turns left",
        "SPRINT*  - Moves forward a great distance",
        "      *  - Requires a magnitude ",
        "REPLAY   - Replays commands with modifiers REVERSED, SILENT and with a range"
        ]

    print("I can understand these commands:")
    for x in commands:
        print(x)

    return robot_data


def save_command(robot_data, command):
    """Saves all movement commands to a list"""

    valid = ["forward", "back", "left", "right", "sprint"]
    movements = robot_data.get('movements')

    command = command.split()
    if command[0].lower() == "left" or command[0].lower() == "right": movements.append(command[0])
    elif command[0] in valid: movements.append(command[0] + " " + command[1])

    robot_data['movements'] = movements
    
    return robot_data


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


def handle_replay(robot_data, command):

    commands = {"replay": 2,"reversed": 0, "silent": 0}
    turn = {"right": turn_right, "left": turn_left}
    move = {"forward": move_forward, "back": move_back, "sprint": sprint}
    command = command.split()
    movements = list(robot_data['movements'])
    reversePrint = ""
    silentPrint = ""
    range1 = 0
    range2 = 0

    for i in command:
        if i.lower() in commands:
            commands[i.lower()] = 2
        elif i.isnumeric(): range1 = len(movements) - int(i)
        elif re.match("\d-\d", i):
            temp = i.split("-")
            if int(temp[0]) > int(temp[1]):
                range1 = len(movements) - int(temp[0])
                range2 = int(temp[1])       
        else: 
            error(robot_data, " ".join(command))
            return robot_data
    
    if commands['reversed'] > 0: 
        movements.reverse()
        reversePrint = " in reverse"

    if commands['silent'] > 0: silentPrint = " silently"

    count = 0
    for i in movements[range1 : len(movements) - range2]:
        i = i.split()
        if i[0] in turn: turn.get(i[0])(robot_data, commands['silent'])
        else: move.get(i[0])(robot_data, i[1], commands['silent'])
        count += 1
    
    print(" > {} replayed ".format(robot_data['name']) + str(count) + " commands" + reversePrint + silentPrint + ".")
    print(" > {} now at position ({},{}).".format(robot_data['name'], robot_data['x'], robot_data['y']))

    return robot_data


def check_command(robot_data):
    """Collects and passes all user commands"""

    noparam_commands = {"off": shut_down, "help": help_command, "right": turn_right, "left": turn_left}
    param_commands = {"forward": move_forward, "back": move_back, "sprint": sprint}

    while robot_data['power'] == True:
        command = input("{}: What must I do next? ".format(robot_data['name']))
        while command == "":
            command = input("{}: What must I do next? ".format(robot_data['name']))
        command = command.split()                       #Turn the input into the list and check the first element for the command
        if command[0].lower() in noparam_commands:      #without the movement magnitude causing errors with the dictionary check
            robot_data = noparam_commands.get(command[0].lower())(robot_data, 0)
            save_command(robot_data, " ".join(command))
        elif command[0].lower() in param_commands:
            if len(command) < 2 or command[1].isnumeric() == False: error(robot_data, " ".join(command))
            else:
                robot_data = param_commands.get(command[0].lower())(robot_data, int(command[1]), 0)
                save_command(robot_data, " ".join(command))
        elif command[0].lower() == "replay": robot_data = handle_replay(robot_data, " ".join(command))
        else: error(robot_data, " ".join(command))
           
    return
    
    
if __name__ == '__main__':
    robot_start()
