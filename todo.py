print("--- My To-Do List ---")
print("1. View Tasks")
print("2. Add Task")
print("3. Quit")

choice = input("Choose an option: ")

if choice == "1":
    print("You selected: View Tasks")
elif choice == "2":
    print("You selected: Add Task")    
elif choice == "3":
    print("Goodbye!")
else:
    print("Hey that wasn't an option! Try again")