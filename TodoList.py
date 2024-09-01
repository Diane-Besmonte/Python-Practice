tasks = []

def programStart():
    print("1 - Display Todo | 2 - Add Task | 3 - Remove Task | 4 - Exit Todo App")
    userChoice = input("What do you want to do? \n:")
    return userChoice

userChoice = programStart()

# Functions
def displayTodo():
    if(len(tasks) == 0):
        print("No tasks added.")
    else:
        for task in tasks:
            print(task)

def addTodo(task):
    tasks.append(task)
    print("Task added:", task)

def removeTodo(task):
    try:
        tasks.remove(task)
        print("Task removed:", task)
    except ValueError:
        print("Item not found on the list.")

while True:
    userChoice = programStart()
    if(userChoice == "1"):
        displayTodo()

    elif(userChoice == "2"):
        task = input("Enter a new task: ")
        addTodo(task)

    elif(userChoice == "3"):
        task = input("Enter a task to remove: ")
        removeTodo(task)

    elif(userChoice == "4"):
        print("Thank you for using todo app.")
        break
    else:
        print("Invalid choice. Please try again.")