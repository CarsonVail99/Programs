def menu(task_list=None):
    if task_list is None:
        task_list = []
    print('WHAT WOULD YOU LIKE TO DO?')
    print('1.ADD TASK')
    print('2.SHOW ALL TASKS')
    print('3.DELETE TASKS')
    print('4.EXIT')
    choice = input('ENTER YOUR CHOICE (1-4): ')
    if choice == '1':
        return add_task(task_list)
    elif choice == '2':
        return show_all_tasks(task_list)
    elif choice == '3':
        return delete_task_func(task_list)
    elif choice == '4':
        print('THANK YOU FOR BEING PRODUCTIVE')
        return None
    else:
        print('INVALID CHOICE')
        return menu()

def add_task(task_list):
    while True:
        task = input('ENTER TASK')
        task_list.append(task)
        add_another_task = input('DO YOU WANT TO ADD ANOTHER TASK? Y/N')
        if add_another_task == 'Y':
            print('TASKS ADDED')
            continue
        elif add_another_task.upper() == 'N':
            return menu(task_list)
        else:
            print('INVALID CHOICE')
            return menu(task_list)


def show_all_tasks(task_list, return_to_menu=True):
    print('YOUR TASKS ARE:')
    if not task_list:
        print('NO TASKS')
    else:
        for index, task in enumerate(task_list, start=1):
            print(f'{index}. {task}')
    if return_to_menu:
        return menu(task_list)

def delete_task_func(task_list):
    if not task_list:
        print('NO TASKS')
        return menu(task_list)

    show_all_tasks(task_list, return_to_menu=False)
    try:
        delete = int(input('ENTER THE TASK YOU WANT TO DELETE:'))
        if 1<= delete <= len(task_list):
            delete_task = task_list.pop(delete-1)
            print(f'TASK {delete_task} DELETED')
        else:
            print('INVALID CHOICE')
    except ValueError:
        print('INVALID CHOICE')
    return menu(task_list)



def main():
    task_list = []
    menu(task_list)



if __name__ == '__main__':
    main()