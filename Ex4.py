# 2D dictionary of tasks to be done
tasks = {'t1': {'todo': 'Call John for AmI project organization', 'urgent': True},
         't2': {'todo': 'buy a new mouse', 'urgent': True},
         't3': {'todo': 'find a present for Angelina’s birthday', 'urgent': False},
         't4': {'todo': 'organize mega party (last week of April)', 'urgent': False},
         't5': {'todo': 'book summer holidays', 'urgent': False},
         't6': {'todo': 'whatsapp Mary for a coffee', 'urgent': False}
         }


urgent_tasks = {}
index = 0

for (name, task) in tasks.items():
    if task['urgent']:
        urgent_tasks[index] = {}  # creating inner dictionary as default one (to-do task and urgency)
        urgent_tasks[index]['todo'] = task['todo']
        urgent_tasks[index]['urgent'] = task['urgent']
        index = index + 1

print("\nUrgent dictionary successfully created with", index, "element(s):")
print(urgent_tasks)
