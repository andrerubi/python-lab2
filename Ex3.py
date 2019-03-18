from sys import argv

file_name = argv[1]
content = open(file_name)
todo = content.read().split('\n')  # creating the list from input file
content.close()

finish = 0  # loop flag
input_msg = """Insert the number corresponding to the action you want to perform:
1. insert a new task;
2. remove tasks from a substr;
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

        word = input("Insert word to be found in the task: ")
        content = open(file_name, "w")
        for task in todo:
            if task.find(word) == -1:   # task not to be deleted
                content.write(task)
                content.write('\n')
            else:
                todo.remove(task)

        content.close()
        print("Task(s) containing '", word, "' removed\n\n")

    elif choice == 3:
        print(sorted(todo), "\n\n")

    elif choice == 4:
        finish = 1
    else:
        print("Error: unrecognized command.\n")
