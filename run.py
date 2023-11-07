
from to_do_list import *
while True:
    print("\nTo-Do Taks")
    print("1. Add a Task")
    print("2. Display Given Task ")
    print("3. Remove a Task")
    print("4. Delete Your TO-DO")
    print("5. Exit")
    option = eval(input("Choose an option: "))

    if option == 1:
        add_task()
    elif option == 2:
        show_task()
    elif option == 3:
        # task_num = int(input("enter a task number to remove from the list: "))
        rmv_task()
    elif option == 4:
        confirmation = input("Are you sure to delete your file: ").lower()
        if confirmation == 'yes':
            delete_file()
            print("Your TO-DO deleted successfully")
    elif option == 5:
        break
    else:
        print("Naughty ho rha bkl")