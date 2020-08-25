
def create_outline(): #This assignment has caused me so much physical pain

    problems = ["Problem 1", "Problem 2", "Problem 3"]    
    topics = {"* Introduction to Python",
            '* Tools of the Trade',
            '* How to make decisions',
            '* How to repeat code',
            '* How to structure data',
            '* Functions',
            '* Modules'}
    status = ["STARTED", "GRADED", "COMPLETED"]
    topics_list = list(topics)
    topics_list = sorted(topics_list)
    topics_dict = {topics_list[0] : problems,   #You can pinpoint the exact moment I stopped caring
                topics_list[1] : problems,
                topics_list[2] : problems,
                topics_list[3] : problems,
                topics_list[4] : problems,
                topics_list[5] : problems,
                topics_list[6] : problems}

    students = [("Fred", topics_list[1], problems[2], status[1]),
                ("Jeff", topics_list[4], problems[0], status[0]),
                ("Sarah", topics_list[0], problems[1], status[2])]
    students.sort(key = lambda x:x[3], reverse = True)

    print("Course Topics:")
    for x in topics_list:
        print(x)
    
    print("Problems:")
    for key, value in topics_dict.items():
        print(key + " : " + ", ".join(value))

    count = 1
    print("Student Progress: ")
    for x in students:
        print(str(count) + ". " + x[0] + " -", x[1], x[2], "- ", "[" + x[3] + "]")
        count += 1


if __name__ == "__main__":
    create_outline()
