from rich.console import Console
from rich.table import Table

console = Console()

def create_table_personal(summary=None, day=None, month=None, hour=None, mins=None):
    """Creates a table with all the user's personal events"""

    table = Table(show_header=True, header_style='green')
    table.add_column("Title", width=20)
    table.add_column("Date  - Time")

    table.add_row(summary,
                "{:02d}/{:02d} - {:02d}:{:02d}".format(day, month, hour, mins))
    
    console.print(table)


def create_table(summary=None, students=None, volunteer=None, day=None, month=None, hour=None, mins=None, event_id=None):
    """Creates a table with all the information needed for the clinic events"""

    table = Table(show_header=True, header_style="bold cyan")
    table.add_column("Topic", width=20)
    table.add_column("Students", width=10)
    table.add_column("Volunteer", width=10)
    table.add_column("Date  - Time")
    table.add_column("Event ID")

    students_str = ""
    if len(students) == 4:
        return create_table_red(summary=summary, students=students, volunteer=volunteer, day=day, month=month, hour=hour, mins=mins, event_id=event_id)
        
    else:
        for student in students:
            if student == volunteer:
                pass
            elif student == students[-1]:
                students_str += student  #Checks for the final student so no new line is added
            else:
                students_str += student + '\n'

    table.add_row(summary,
                students_str,
                volunteer,
                "{:02d}/{:02d} - {:02d}:{:02d}".format(day, month, hour, mins),
                event_id)
    
    console.print(table)


def create_table_red(summary=None, students=None, volunteer=None, day=None, month=None, hour=None, mins=None, event_id=None):
    """Creates a table with all the information needed for the clinic events"""

    table = Table(show_header=True, header_style="bold red")
    table.add_column("Topic", width=20)
    table.add_column("Students", width=10)
    table.add_column("Volunteer", width=10)
    table.add_column("Date  - Time")
    table.add_column("Event ID")

    students_str = ""
    for student in students:
        if student == volunteer:
            pass
        elif student == students[-1]:
            students_str += student  #Checks for the final student so no new line is added
        else:
            students_str += student + '\n'

    table.add_row(summary,
                students_str,
                volunteer,
                "{:02d}/{:02d} - {:02d}:{:02d}".format(day, month, hour, mins),
                event_id)
    
    console.print(table)