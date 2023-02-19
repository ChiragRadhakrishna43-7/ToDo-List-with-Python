# from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(now)
while True:
    action = input("Menu: 1. ADD 2. SHOW 3. EDIT 4. COMPLETE 5. EXIT ")
    action = action.strip()

    if action.startswith('add'):
        todo = action[4:]
        todos = functions.get_todos()
        todos.append(todo + '\n')
        functions.write_todos(todos)

    elif action.startswith('show'):
        todos = functions.get_todos()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}-{item}"
            print(row)

    elif action.startswith('edit'):
        try:
            number = int(action[5:])
            number = number - 1
            todos = functions.get_todos()
            todo1 = input('Enter new todo: ')
            todos[number] = todo1 + '\n'
            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid")
            continue

    elif action.startswith('complete'):
        try:
            number = int(action[9:])
            todos = functions.get_todos()
            index = number-1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            functions.write_todos(todos)
            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no such entry with this number")
            continue

    elif action.startswith('exit'):
        break

    else:
        print("Command is not valid")

