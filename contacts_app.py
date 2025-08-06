def menu():
    print('='*10,'Contact App','='*10)
    print('1.Add Contacts')
    print('2.View Contacts')
    print('3.Search Contacts')
    print('4.Update Contacts')
    print('5.Delete Contacts')
    print('6.Exit')
    choice = int(input('Enter your choice: '))
    return choice

def add_contact(contact_list):
    while True:
        name = input('Enter contact name: ')
        phone = input('Enter contact number: ')
        contact_list[name] = int(phone)
        prompt = input('Do you want to add another contact? (y/n): ')
        if prompt == 'y':
            add_contact(contact_list)
            return contact_list, add_contact
        elif prompt == 'n':
            return contact_list, add_contact, False
        else:
            print('Invalid choice')
            return False

def view_contacts(contact_list):
    if contact_list:
        print('All Contacts:\n')
        for name, phone in contact_list.items():
            print(f'Contact name: {name}, Phone number: {phone}')
    else:
        print('No contacts found')



def search_contact(contact_list):
    search_number = input('Enter contact name to search: ')
    search_number = contact_list.get(search_number)
    if search_number: print(f'Phone number: {search_number}')
    else: print('Contact not found')
    return None

def update_contact(contact_list):
    update_name = input('Enter contact name to update: ')
    if update_name in contact_list:
        update_phone = input('Enter new number: ')
        contact_list[update_name] = int(update_phone)
        return contact_list
    else:
        print('Contact not found')
        return None

def delete_contact(contact_list):
    delete_name = input('Enter contact name to delete: ')
    if delete_name in contact_list:
        delete_name = contact_list.pop(delete_name)
        print(f'Contact {delete_name} deleted')
        return delete_name
    else:
        print('Contact not found')
        return None

def exit():
    print('Thanks for using Contact App')
    return None

def main():
    contact_list = {}
    while True:
        choice = menu()
        if choice == 1:
            add_contact(contact_list)
        elif choice == 2:
            view_contacts(contact_list)
        elif choice == 3:
            search_contact(contact_list)
        elif choice == 4:
            update_contact(contact_list)
        elif choice == 5:
            delete_contact(contact_list)
        elif choice == 6:
            exit()
            break

if __name__ == '__main__':
    main()






