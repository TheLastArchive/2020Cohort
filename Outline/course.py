

def create_outline():

    problems = ["Problem 1", "Problem 2", "Problem 3"]    
    topics = {"* Introduction to Python": problems,
            '* Tools of the Trade': problems,
            '* How to make decisions': problems,
            '* How to repeat code': problems,
            '* How to structure data': problems,
            '* Functions': problems,
            '* Modules': problems}
    status = ["STARTED", "GRADED", "COMPLETED"]

    fred = (1, "Fred", "Modules", status[1])
    jeff = (2, "Jeff", "Functions", status[0])
    victoria = (3, "Victoria", "How to repeat code", status[2])
    students = [fred, jeff, victoria]

    print("Course Topics:")
    for x in topics:
        print(x)
    
    print("Problems:")
    for key, value in topics.items():
        print(key + ": " + ", ".join(value))

    print("Student Progress: ")
    for x in students:
        print(str(x[0]) + ".", x[1] + " -", x[2], "[" + x[3] + "]")


if __name__ == "__main__":
    create_outline()
