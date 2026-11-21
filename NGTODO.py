print("===to do list===")

tasks = []

while True:
    print("/ntask to be done")
    print("1.add the task")
    print("2.view tasks")
    print("3.delete tasks")
    print("4.exit")

    choice = input("enter the option(1-4):")

    if choice == "1":
        task =input("enter new task")
        tasks.append(task)
        print("task added")
    elif choice == "2":
        if len(tasks) == 0:
            print("no tasks")
        else:
             for i in range(len(tasks)):
                 print(i+1,".",tasks[i])
    elif choice == "3":
        if len(tasks) == 0:
            print("no task to delete")
        else:
            removed = tasks.pop(1)
            print("deleted =", removed)
    elif choice == "4":
        break
    
    else:
        print("invalid inputs")
        
            

           

