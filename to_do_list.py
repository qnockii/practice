todo_list = ["Esen", "Trinken", "Schlafen"]

def show_list(todo_list):
    return(todo_list)

def get_next_action():
    global next_action  
    next_action = input("Add a task to list: ")

def type_error():
    print("Type.Error=Please Type a valid variable.")

def list_add_task(next_action):
    todo_list.append(next_action)
    return todo_list

def list_remove_task(todo_list):
    rm = input("Enter task you want remove: ")
    for rm in todo_list:
        todo_list.remove(rm)
    return todo_list

def list_edit_task(todo_list):
    edit = input("Type to edit task: ")
    for edit in todo_list:
        edit = input("Typ edited task:")
    return todo_list

to_do_list = True
while to_do_list:
    print("What do you want to do?")
    print(" 'watch', 'add', 'remove' or 'edit' a task or 'quit' the loop?")
    get_next_action = input("Type here: ")

    if get_next_action == "watch" or get_next_action == "Watch":
        show_list(todo_list)
    elif get_next_action == "add" or get_next_action == "Add":
         list_add_task(todo_list)
         print("Added.")
    elif get_next_action == "remove" or get_next_action == "Remove":
        list_remove_task(todo_list)
        print("Removed.")
    elif get_next_action == "edit" or get_next_action == "Edit":
        list_edit_task(todo_list)
        print("Edited.")
    elif get_next_action == "quit" or get_next_action == "Quit":
         to_do_list = False
         print("You left the loop.")
    else:
        type_error()