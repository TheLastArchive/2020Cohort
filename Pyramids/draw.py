

# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():

    shape_param = input("Shape?: ")

    while shape_param.lower() not in ["square", "triangle", "pyramid", "rhombus"]:
       shape_param = input("Shape?: ")
       

    return shape_param.lower()


# TODO: Step 1 - get height (it must be int!)
def get_height():
    
    height_param = input("Height?: ")

    while height_param.isnumeric() == False:
        height_param = input("Height?: ")
    while int(height_param) > 80 or int(height_param) < 1:
        height_param = input("Height?: ")         

    return int(height_param)


# TODO: Step 2
def draw_pyramid(height, outline):

    star = "*"
    star_count = 1
    space = " "
    space_count = height - 1
    count = 0
    space_count2 = 1

    if outline == False:
        while (height != count):
            print((space * space_count) + (star * star_count))
            star_count += 2
            space_count -= 1
            count += 1
    else:
        print(space * space_count + star)
        space_count -= 1
        while (height - 2 != count):
            print((space * space_count) + star + (space * space_count2) + star)
            space_count -= 1
            space_count2 += 2
            count += 1

        print(star * (space_count2 + 2))



# TODO: Step 3
def draw_square(height, outline):

    star = "*"
    space = " "
    count = 0

    if outline == False:
        while (count != height):
            print(star * height)
            count += 1

    else:
        if height == 1:
            print(star)
        else:
            print(star * height)
            count += 1
            while (count != height - 1):
             print (star + space * (height - 2) + star)
             count += 1
            print (star * height)



# TODO: Step 4
def draw_triangle(height, outline):

    star = "*"
    star_count = 1
    space = " "
    space_count = 0
    count = 0

    if outline == False:
        while (count != height):
            print(star * star_count)
            star_count += 1
            count += 1

    else:
        print(star)
        count += 1
        while (count != height - 1):
            print(star + (space * space_count) + star)
            space_count += 1
            count += 1
        print(star * height)


def draw_rhombus(height, outline):

    count = 0
    space_count = height - 1

    if outline == False:
        while count != height:
            print(" " * space_count + "*" * height)
            count += 1
            space_count -= 1
    else:
        print(" " * space_count + "*" * height)
        count += 1
        space_count -= 1
        while count != height - 1:
            print(" " * space_count + "*" + " " * (height - 2 ) + "*")
            space_count -= 1
            count += 1
        print("*" * height)


# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):

    if (shape == "pyramid"):
        draw_pyramid(height, outline)
    elif (shape == "square"):
        draw_square(height, outline)
    elif (shape == "triangle"):
        draw_triangle(height, outline)
    elif (shape == "rhombus"):
        draw_rhombus(height, outline)
    

# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():

    outline_param = input("Outline only? (y/n): ")

    while outline_param not in ["y", "n"]:
        outline_param = input("Outline only? (y/n): ")

    if outline_param == "y":
        return True
    else:
        return False


if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)

