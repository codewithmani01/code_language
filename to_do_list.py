import os
file_name = "to-do-list.txt"

to_do_list = []
def add_task():
    while True:
        task = input("Enter Your Tasks For Today or 'done' to Exit: ")
        if task.lower() == 'done':
            break
        else:
            tasks = to_do_list.append(task)
    file = open(file_name, "a")
    for task in to_do_list:
        file.write(task + '\n')
    file.close()

def show_task():
    file = open(file_name, 'r')
    tasks = file.readlines()
    if not tasks:
        print("there is no tasks to do.")
    else:
        print("tasks in to do list.")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}: {task.strip()}")
    file.close()

def rmv_task():
    while True:
        file = open(file_name, 'r')
        tasks = file.readlines()
        if not tasks:
            print("there is no tasks to do.")
        else:
            print("Choose the number of Task you want to remove")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}: {task.strip()}")
        file.close()

        task_num = int(input("Enter the task number to remvove the task: "))
        read_file = open(file_name, 'r')
        tasks = read_file.readlines()
        if 1 <= task_num <= len(tasks):
            file = open(file_name, 'w')
            tasks.pop(task_num-1)
            file.writelines(tasks)
            print("Task removed succesfully")
            break
        else:
            print("Invalid Task Numbver")
def delete_file():
    os.remove(file_name)
    print("file deleted successfully")


