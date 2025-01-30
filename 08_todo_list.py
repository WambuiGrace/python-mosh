'''
Loop
    print menu for user input
    choice ==1 "display tasks"
    choice ==2 "user adds a task"
    choice ==3 "user deletes a task, removed from list"
    choice ==4 "exit"
'''
def display_menu():
    print("\n Todo List Menu:")
    print("1. Display tasks")
    print("2. Add a task")
    print("3. Delete a task")
    print("4. Exit")

# Get user choice
def get_choice():
    while True:
        choice = input("Enter your choice (1-4): ")
        valid_choices = ('1', '2', '3', '4')

        if choice not in valid_choices:
            print('Invalid choice. Try again.')
            continue
        else:
            return choice

# Display user tasks
def display_tasks(tasks):
    if not tasks:
        print('No tasks in the list.')
        return
    for index,task in enumerate(tasks, start=1):
        print(f'{index}. {task}')

# Add task to to-do list
def add_task(tasks):
    while True:
        task = input('Enter a task: ').strip()
        if len(task) != 0:
            tasks.append(task)
            break
        else:
            print('Invalid input.')
        print('Task added')

def delete_task(tasks):
    display_tasks(tasks)
    while True:
        try:
            task_number = int(input('Enter the number of the task to delete: '))
            if 1 <= task_number <= len(tasks):
                tasks.pop(task_number - 1)
                break
            else:
                raise ValueError
        except ValueError:
            print('Invalid input. Please enter a number.')
            
    print('Task deleted')

def main ():
    tasks = []
    while True:
        display_menu()

        choice = get_choice()

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            delete_task(tasks)
        else:   
            print('Goodbye')
            break

if __name__ == "__main__":
    main() 