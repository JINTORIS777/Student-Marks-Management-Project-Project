# Part 1: Single student results
studentName = input("Enter your name: ")
Markstudent1 = float(input("Enter your mark 1: "))
Markstudent2 = float(input("Enter your mark 2: "))
Markstudent3 = float(input("Enter your mark 3: "))

aveRage = (Markstudent1 + Markstudent2 + Markstudent3) / 3

if (Markstudent1 >= Markstudent2) and (Markstudent1 >= Markstudent3):
    largest = Markstudent1 
elif (Markstudent2 > Markstudent1) and (Markstudent2 >= Markstudent3):
    largest = Markstudent2
else:
    largest = Markstudent3

total = Markstudent1 + Markstudent2 + Markstudent3

print("Thank you, here are your results:")
print("Average:", aveRage)
print("Highest mark:", largest)
print("Total Marks:", total)


# Part 2: Multiple students data entry
students = dict()
n = int(input("Enter the number of students: "))
for i in range(n):
    name = input(f"Enter the name of student #{i+1}: ")
    marks = []
    for j in range(5):
        mark = float(input(f"Enter mark #{j+1} for {name}: "))
        marks.append(mark)
    students[name] = marks

print("\nAll student data:")
for student, marks in students.items():
    print(f"{student}: {marks}")
