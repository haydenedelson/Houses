from sys import argv, exit
from cs50 import SQL
import csv

# Check for proper arguments
if len(argv) != 2:
    print("Error: Usage: python import.py [filename].csv")
    exit(1)

# Open SQL database
db = SQL("sqlite:///students.db")

def main():

    # Open CSV file
    # Create reader object
    with open(argv[1], newline='') as students_file:
        students_file.readline()
        students_reader = csv.reader(students_file)

        # For each student in CSV file, write info to SQL database
        for row in students_reader:
            write_to_database(row)

# For each student, pass in list with three arguments: name, house, birth year
def write_to_database(curr_student):
    # For each student, split name into [first, last] or [first, middle, last]
    # Store house, & convert birth year to integer to match db structure
    name = curr_student[0].split(' ')
    house = curr_student[1]
    birth = int(curr_student[2])

    # If no middle name, pass None as middle name value
    if len(name) == 2:
        db.execute("INSERT INTO students(first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?);",
                    (name[0], None, name[1], house, birth))
    else:
        db.execute("INSERT INTO students(first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?);",
                    (name[0], name[1], name[2], house, birth))


main()
