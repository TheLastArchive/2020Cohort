
def move_square(size):

    print("Moving in a square of size "+str(size))
    for i in range(4):
        degrees = 90
        print("* Move Forward "+str(size))
        print("* Turn Right "+str(degrees)+" degrees")


def move_rectangle(length, width):

    print("Moving in a rectangle of "+str(length)+" by "+str(width))
    for i in range(2):
        degrees = 90
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")
        print("* Move Forward "+str(width))
        print("* Turn Right "+str(degrees)+" degrees")
    

def move_circle(degrees):

    print("Moving in a circle")
    for i in range(360):
        length = 1
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")

def square_dance(size, degrees):
    
    print("Square dancing - 3 squares of size 20")
    for i in range(3):
        length = 20
        print("* Move Forward "+str(length))
        #print("Moving in a square of size " + str(length))
        move_square(length)

def crop_circles(length, degrees):

    print("Crop circles - 4 circles")
    for i in range(4):
        print("* Move Forward "+str(length))
        
        move_circle(degrees)

# TODO: Decompose into functions
def move(): #def robot_controller() as this function is used to direct the robot
            #into it's specific actions
    size = 10
    length = 20
    width = 10
    degrees = 1

    move_square(size)
    move_rectangle(length, width)
    move_circle(degrees)
    square_dance(size, degrees)
    crop_circles(length, degrees)

def robot_start():
    move()


if __name__ == "__main__":
    robot_start()
