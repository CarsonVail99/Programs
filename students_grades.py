import sys
import time

class Student_class:
    student_count = 0
    students = []

    def add_student(self):
        add_info = {}
        add_info['First name'] = input('Enter first name: ').capitalize()
        add_info['Last name'] = input('Enter last name: ').capitalize()
        add_info['Grade'] = input('Enter grade: ').upper()
        if add_info['Grade'] not in ['A','B','C','D','F']:
            print('Invalid grade')
            return None
        else:
            gpa_map = {'A':4.0,'B':3.0,'C':2.0,'D':1.0,'F':0.0}
            add_info['gpa'] = gpa_map[add_info['Grade']]
            Student_class.students.append(add_info)
            Student_class.student_count += 1
        for key, value in add_info.items():
            print(f'{key} : {value}')
        return add_info

    def show_all_students(self):
        print('All students:')
        print(f'Total students: {Student_class.student_count}')
        for student in Student_class.students:
            print('------------------------------------')
            for key, value in student.items():
                print(f'{key} : {value}')
        return None

    def delete_student(self):
        while True:
            search_option = input('Enter first or last name: ').capitalize()
            for student in Student_class.students:
                if search_option in [student['First name'], student['Last name']]:
                    print('Student found')
                    Student_class.students.remove(student)
                    Student_class.student_count -= 1
                    delete_more = input('Do you want to delete more students? (y/n): ').lower()
                    if delete_more in ['y','yes']:
                        continue
                    else:
                        break
            return Student_class.students


    def menu(self):
        while True:
            print("---------Student system menu---------")
            print("1. Add student")
            print("2. Delete student")
            print("3. Show all students")
            print("4. Save and Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.delete_student()
            elif choice == "3":
                self.show_all_students()
            elif choice == "4":
                self.save_data()
                print("Data saved successfully.")
                print("Exiting the program...")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def save_data(self):
        with open('students.txt', 'a') as f:
            for student in Student_class.students:
                for key, value in student.items():
                    f.write(f'{key} : {value}\n')









def main():
    student_system = Student_class()
    student_system.menu()


if __name__ == '__main__':
    main()
