filename="tasks.txt"
def load_tasks():
    try:
        tasks=[]
        with open(filename,"r") as f:
            for line in f:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass
    return tasks
def save_tasks(tasks):
    with open(filename,"w") as f:
        for t in tasks:
            f.write(t+"\n")
    
def add(data):
    tasks.append(data)
    save_tasks(tasks)
    print("Task added")
def view(tasks):
    if not tasks:
        print("No tasks yet")
    else:
        print("Your tasks:")
        for i in range(len(tasks)):
            print(tasks[i])
def update(tasks):
    if not tasks:
        print("No tasks to be updated")
    else:
        print("To update the task!")
        num=int(input("Enter the number: "))
        new_task=input("Enter the task to be updated")
        tasks[num]=new_task
        save_tasks(tasks)
        print("The updated task list")
        for i in range(len(tasks)):
            print(tasks[i])
def delete(task):
    if not task:
        print("No task to delete")
    else:
        print("To delete a task!")
        num=int(input("Enter the number of the task to be deleted:"))
        del task[num]
        save_tasks(tasks)
        print("The task list")
        for i in range(len(task)):
            print(task[i])
        
    


if __name__=="__main__":
    tasks=load_tasks()
    while True:
        print("1.Add Task")
        print("2.View Task")
        print("3.Update Task")
        print("4.Delete Task")
        print("5.Exit")
        choice=input("Enter the choice:")
        match choice:
            case '1':
                data=input("Enter the task:")
                add(data)
            case '2':
                view(tasks)
            case '3':
                update(tasks)
            case '4':
                delete(tasks)
            case '5':
                print("Goodbye!!!")
                break

            
        


