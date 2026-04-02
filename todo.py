tasks = []

while True:
    print("--- My To-Do List ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Quit")

    choice = input("Choose an option [1-3]: ")

    if choice == "1":
        if len(tasks) == 0:
            task = input("There are no tasks yet, would you like to add one? [Y / N]")
            if task == "Y":
                        task = input("Enter your task: ")
                        tasks.append(task)
                        print("Task added.")
            elif task == "N":
                print("Sounds good.")  
        else:
            for i, task in enumerate(tasks):
                print("Here are your saved tasks.")
                print (i +1, task)          
    elif choice == "2":
        task = input("Enter your task: ")
        tasks.append(task)
        print("Task added.")    
    elif choice == "3":
        print("Goodbye!")
    elif choice == "hello":
        print("Nice to meet you, but please choose a number now!")
    else:
        print("Hey that wasn't an option! Try again")