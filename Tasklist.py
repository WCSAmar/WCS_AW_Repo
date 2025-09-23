# Develop a simple task list manager that allows users to add, remove, and view tasks. 
# The program should save the task list to a text file and handle exceptions in a controlled manner
#=========================================================================================
#function to add tasks to the list.
#function to remove completed tasks
#function to view the current task list
#function to save and load tasks from a file
#function to handle exceptions for file read/write errors
#==========================================================================================

#function to add tasks to the list
def add_task(tasks):
    task = input("Enter task description: ")
    tasks.append(task)
    print("Task added to the list successfully")
    
#function to view task
def view_task(tasks):
    for index, task in enumerate(tasks, start = 1):
        print(f"{index}. {task}")

#function to remove completed task
def task_completed(tasks):
    if not tasks:
        print("Tasks are still in progress...")
    view_task(tasks)
    index = int(input("Enter task index to mark as completed: ")) - 1

    if 0<= index < len(tasks):
        remove_task = tasks.pop(index)
        print(f"Completed task removed")
    else:
        print(f"Invalid index")

#load task file
def load_task_file():
    try:
        with open("tasks.txt", "r") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return[]
    
#save task to file
def save_task(tasks):
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + '\n')

            
def main():

    tasks = load_task_file() #task list

    while True:
        print("Select the task operation - add/remove/view/exit")
        print("1. Add Task")
        print("2. View Task")
        print("3. Remove Task")
        print("4. Exit")

        select = input("Select operation: ")

        if select == '1':
            add_task(tasks)
        elif select == '2':
            view_task(tasks)
        elif select == '3':
            task_completed(tasks)
        elif select == '4':
            save_task(tasks)
            break
        else:
            print("Invalid selection. Please select valid option.")
main()
