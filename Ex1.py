input_msg = """Insert the number corresponding to the action you want to perform:
1. insert a new task;
2. remove a task;
3. show all the tasks;
4. close the program.
Your choice: """
todo = ["Study", "Eat", "Go to the gym"]  # to do list
finish = 0

while not finish:
    choice = int(input(input_msg))
    if choice == 1:
        task = input("Insert new task: ")
        todo.append(task)
        print(task, "added\n\n")

    elif choice == 2:

        task = input("Insert task to be deleted: ")
        try:
            todo.remove(task)
            print(task, "removed\n\n")
        except ValueError:
            print(task, "not found\n\n")

    elif choice == 3:
        print(sorted(todo), "\n\n")

    elif choice == 4:
        finish = 1
    else:
        print("Error: unrecognized command.\n")
