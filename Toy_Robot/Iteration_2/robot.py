
def robot_start():
    """This is the entry function, do not change"""

    name_robot()
    check_command()
    pass

def name_robot():
    """Names the robot"""

    global name 
    name = input("What do you want to name your robot? ")
    print(name + ": Hello kiddo!")


def error(command):

    print(name + ": Sorry, I don't understand '{}'.".format(command))

def shut_down(command):

    print(name + ": Shutting down..")

    return False

def help_command(command):

    commands = ["OFF  - Shut down robot", "HELP - Provide information about commands"]
    print("I can understand the following commands:")
    for x in commands:
        print(x)

    return True

    
def check_command():

    commands = {
        "off": shut_down,
        "help": help_command,
        }

    cont = True
    while cont == True:
        command = input(name + ": What must I do next? ")
        while command.lower() not in commands:
            error(command)
            command = input(name + ": What must I do next? ")
        cont = commands.get(command.lower(), error)(command)


if __name__ == "__main__":
    robot_start()
