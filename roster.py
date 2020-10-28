from sys import argv, exit
from cs50 import SQL

# Check for proper arguments
if len(argv) != 2:
    print("Error: Usage: python roster.py [House]")
    exit(1)

db = SQL("sqlite:///students.db")


# Select name and birth year, ordered by last name then first name
roster = db.execute("SELECT first, middle, last, birth FROM students WHERE house = ? ORDER BY last, first;", argv[1].title())

# For each student, print "[Student's Name], born [birth year]"
for student in roster:
    if student['middle'] == None:
        print(f"{student['first']} {student['last']}, born {student['birth']}")
    else:
        print(f"{student['first']} {student['middle']} {student['last']}, born {student['birth']}")
