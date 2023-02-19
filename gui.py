import functions
import PySimpleGUI as sg
import time


sg.theme("Black")
clock = sg.Text('', key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo", size=[46,10])
add = sg.Button("Add", size=10)
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[45,9])
edit = sg.Button("Edit", size=10)
complete = sg.Button("Complete", size=10)
exitButton = sg.Button("Exit", size=10)

window = sg.Window("My To-Do App",
                   layout=[[clock], [label], [input_box, add], [list_box, edit, complete], [exitButton]],
                   font=('Agency FB', 20))

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 20))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value=' ')
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 20))
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break


window.close()
