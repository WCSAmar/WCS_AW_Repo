#  Build a program that helps students track their grades. Students can input the grades they achieve for each subject,
#  and the program will read their grades from a file and calculate their average grade. The program should handle exceptions 
# (e.g., invalid input, file errors) and store the grades in a file for future reference.
#

#write student name, courses and grades to a file
def write_student_data_to_file(filename, student_data):
    with open(filename, 'w') as file:
        for student_name, courses in student_data.items():
            line = f"{student_name}:"
            course_grade_pairs = []
            for course, grade in courses.items():
                course_grade_pairs.append(f"{course},{grade}")
            line += ";".join(course_grade_pairs)
            file.write(line + "\n")

#Reading the Nested Dictionary from a file:
def read_student_data_from_file(filename):
    student_data = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                parts = line.split(':', 1)
                student_name = parts[0]
                courses_str = parts[1] if len(parts) > 1 else ""

                student_data[student_name] = {}
                if courses_str:
                    course_grade_pairs = courses_str.split(';')
                    for pair in course_grade_pairs:
                        if ',' in pair:
                            course, grade = pair.split(',')
                            student_data[student_name][course] = grade
        return student_data
    except FileNotFoundError:
        return {}

def main():
    
    file_name = "grades.txt"
    total = 0
    i = 0
    student_dict = {}

    #User to input student data 
    print("Please enter student name, course name and respective grades:\n")
    while True:
        student_name = input("Enter student name (or 'done' to finish): ").strip()
        if student_name.lower() == 'done':
            break

        student_dict[student_name] = {}

        while True:
            course_name = input(f"Enter course name for {student_name}: ")
            if course_name.lower() == 'done':
                break
            try:
                grade = input(f"Grade for {course_name}: ")
                student_dict[student_name][course_name] = grade
            except ValueError:
                print("Invalid input. Please enter percent marks for grade value")

    #Write student data to a file    
    write_student_data_to_file(file_name, student_dict)
    
    # Read data from file
    loaded_students = read_student_data_from_file(file_name)
    
    print("\nLoad student data:")
    for student, courses in loaded_students.items():
        if student:
            for grade in courses.values():
                total += int(grade)
                i = i + 1
                j = total/i
        print(f"Average Grade for {student} is",round(j,2))
    
main()
     

