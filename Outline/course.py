

def create_outline():
    
    topics = {"* Introduction to Python":'',
            '* Tools of the Trade':'',
            '* How to make decisions':'',
            '* How to repeat code':'',
            '* How to structure data':'',
            '* Functions':'',
            '* Modules':''}

    problems = ["Problem 1", "Problem 2", "Problem 3"]

    print("Course Topics:")
    for x in topics:
        print(x)

if __name__ == "__main__":
    create_outline()
