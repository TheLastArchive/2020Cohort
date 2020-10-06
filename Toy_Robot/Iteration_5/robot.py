import re
import sys
from maze import obstacles

if len(sys.argv) > 1 and sys.argv[1] == 'turtle':
    from world.turtle import world
else:
    from world.text import world


def robot_start():
    """This is the entry function, do not change"""

    robot_data = {'name': "", 'x': 0, 'y': 0, 'compass': [1, 2, -1, -2], 'power': True, 'movements': []}
    
    obstacles.create_obstacles()
    robot_data['name'] = name_robot()
    obstacle_list = obstacles.get_obstacles()
    world.display_obstacles(obstacle_list)
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
    obstacles.reset_obstacles() #to reset the obstacle list because they want us to use global variables :)

    return robot_data
    

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


def handle_replay(robot_data, command):

    commands = {"replay": 2, "reversed": 0, "silent": 0}
    turn = {"right": world.turn_right, "left": world.turn_left}
    move = {"forward": world.move_forward, "back": world.move_back, "sprint": world.sprint}
    command = command.split()
    movements = list(robot_data['movements'])

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

    count = 0
    for i in movements[range1 : len(movements) - range2]:
        i = i.split()
        if i[0] in turn: turn.get(i[0])(robot_data, commands['silent'])
        else: move.get(i[0])(robot_data, i[1], commands['silent'])
        count += 1
    
    world.replay_output(robot_data, commands, count)
    
    return robot_data


def check_command(robot_data):
    """Collects and passes all user commands. I'll clean this up one day""" 

    noparam_commands = {"off": shut_down, "help": help_command, "right": world.turn_right, "left": world.turn_left}
    param_commands = {"forward": world.move_forward, "back": world.move_back, "sprint": world.sprint}

    while robot_data['power'] == True:
        command = input(f"{robot_data['name']}: What must I do next? ")
        while command == "":
            command = input(f"{robot_data['name']}: What must I do next? ")
        command = command.split()
        if command[0].lower() in noparam_commands:      
            robot_data = noparam_commands.get(command[0].lower())(robot_data, 0)
            save_command(robot_data, " ".join(command))
        elif command[0].lower() in param_commands:
            if len(command) < 2 or command[1].isnumeric() == False: error(robot_data, " ".join(command))
            else:
                robot_data = param_commands.get(command[0].lower())(robot_data, int(command[1]), 0)
                save_command(robot_data, " ".join(command))
                
        elif command[0].lower() == "replay":
            robot_data = handle_replay(robot_data, " ".join(command))
        else: error(robot_data, " ".join(command))
           
    return
    
    
if __name__ == '__main__':

    robot_start()
    
