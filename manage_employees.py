#Instance methods = Most common method can use .self
#first parameter is self
#can access and modify both instance state and class state
#called on by - object.method_name()

#Class methods = A method that belongs to a class
#First parameter is Class
#Cannot change instance Data
#Called on by - Class.method_name()

#Static methods = A method that doesn't use self or cls
#Called on by - Class.method_name()


class Company101:
    company = "NewCorp" #Class attribute

    def __init__(self, name, position): #Constructor
        self.name = name
        self.position = position

    def get_info(self): #Instance method - called by object.method_name()
        return f"{self.name} == {self.position}"

    @classmethod
    def get_company(cls): #Class method - can access class attributes - Class.method_name()
        print(f"Company name: {cls.company}")

    @classmethod
    def change_company(cls):
        new_company = input('Enter new company name:')
        Company101.company = new_company
        print(f"New Company name: {Company101.company}")
        return Company101.company

    @staticmethod #Standalone method utility function - Does not use self or cls - Class.method_name()
    def open_positions():
        positions = ["Developer", "Manager", "Cashier"]
        return positions


    @classmethod
    def menu(cls):
        while True:
            choice = input('Enter your choice:(1-7)'
                   '\n1. Get company name'
                   '\n2. Change company'
                   '\n3. Open positions'
                   '\n4. Show list of employees'
                   '\n5. Add employee'
                   '\n6. Remove employee'
                   '\n7. Remove Position'
                   '\n8. Exit\n')
            if choice == '1':
                Company101.get_company()
                return False
            elif choice == '2':
                Company101.change_company()
                return False
            elif choice == '3':
                for i in Company101.open_positions():
                    print(i)
                return False
            elif choice == '4':
                for i in employee_list:
                    print(i.get_info())
            elif choice == '5':
                employee_name = input('Enter employee name:')
                employee_position = input('Enter employee position:')
                if employee_position in Company101.open_positions():
                    employee_list.append(Company101(employee_name, employee_position))
                else:
                    print(f'Position {employee_position} not found')
                    return None
            elif choice == '6':
                employee_name = input('Enter employee name:')
                for employee in employee_list:
                    if employee_name == employee.name:
                        employee_list.remove(employee)
                        print(f"Employee {employee_name} removed")
                        return employee_list
                    else:
                        print(f"Employee {employee_name} not found")
                        return None
            elif choice == '7':
                position_to_remove = input('Enter position to remove:')
                positions = Company101.open_positions()
                if position_to_remove in positions:
                    Company101.open_positions().remove(position_to_remove)
                    print(f'Position {position_to_remove} removed')
                    return employee_list
                else:
                    print(f'Position {position_to_remove} not found')
                    return employee_list
            elif choice == '8':
                print('Exiting...')
                break
            else:
                print('Invalid choice')
                return None


employee1 = Company101("John", "Developer")
employee2 = Company101("Jane", "Manager")
employee3 = Company101("Bob", "Clerk")
employee_list = [employee1, employee2, employee3]



def main():
    while True:
        menu = Company101.menu()

if __name__ == "__main__":
    main()

