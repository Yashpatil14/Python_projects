# 1. Challenge: Student Marks Analyzer

class StudentAnalyzer:
    def __init__(self):
        self.students = {}  

    def add_student(self, name, marks):
        if name in self.students:
            print("Duplicate name! Student already exists.")
        else:
            self.students[name] = marks

    def show_report(self):
        if not self.students:
            print("No data available!")
            return

        marks_list = list(self.students.values())
        avg = sum(marks_list) / len(marks_list)
        highest = max(marks_list)
        lowest = min(marks_list)

        highest_students = [name for name, m in self.students.items() if m == highest]
        lowest_students = [name for name, m in self.students.items() if m == lowest]

        
        print("\n========== STUDENT REPORT ==========")
        print(f"Total Students : {len(self.students)}")
        print(f"Average Marks  : {avg:.2f}")
        print("-----------------------------------")
        print(f"Highest Marks  : {highest}")
        print("Topper(s)      :", ", ".join(highest_students))
        print("-----------------------------------")
        print(f"Lowest Marks   : {lowest}")
        print("Lowest Scorer(s):", ", ".join(lowest_students))
        print("===================================")


analyzer = StudentAnalyzer()

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    analyzer.add_student(name, marks)

analyzer.show_report()