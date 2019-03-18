from sys import argv

file_name = argv[1]
content = open(file_name)
todo = content.read().split('\n')  # creating the list from input file
content.close()

finish = 0  # loop flag
input_msg = """Insert the number corresponding to the action you want to perform:
1. insert a new task;
2. remove a task;
3. show all the tasks;
4. close the program.
Your choice: """

while not finish:
    choice = int(input(input_msg))
    if choice == 1:
        task = input("Insert new task: ")

        content = open(file_name, "a")
        content.write(task)
        content.write('\n')
        todo.append(task)
        content.close()

        print(task, "added to the list\n\n")

    elif choice == 2:

        task = input("Insert task to be deleted: ")
        try:
            todo.remove(task)
            content = open(file_name, "w")

            for t in todo:
                content.write(t)
                content.write('\n')

            content.close()
            print(task, "removed from the list\n\n")

        except ValueError:
            print(task, "not found\n\n")

    elif choice == 3:
        print(sorted(todo), "\n\n")

    elif choice == 4:
        finish = 1
    else:
        print("Error: unrecognized command.\n")
