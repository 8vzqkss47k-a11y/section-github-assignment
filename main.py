# Student Grade Calculator

print("Welcome to the Student Grade Calculator!")

# Get the student's name
student_name = input("Enter your name: ")

# Enter grades for three subjects
grade1 = float(input("Enter your first subject grade: "))
grade2 = float(input("Enter your second subject grade: "))
grade3 = float(input("Enter your third subject grade: "))

# Calculate the average
average = (grade1 + grade2 + grade3) / 3

# Display the results
print("\n------ Student Results ------")
print(f"Student Name: {student_name}")
print(f"Average Grade: {average:.2f}")

# Check if the student passed or failed
if average >= 50:
    print("Result: PASS")
else:
    print("Result: FAIL")

print("-----------------------------")
