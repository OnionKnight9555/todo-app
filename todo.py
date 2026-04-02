tasks = []

while True:
    print("--- My To-Do List ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Quit")

    choice = input("Choose an option [1-3]: ")

    if choice == "1":
        print("You selected: View Tasks")
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