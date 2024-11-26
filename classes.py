class todolist:
    def __init__(self):
        self.tasks = []

    def print_todo_list(self):
        print(self.tasks)
        return self.tasks 
 
    def add_task_to_list(self, print_todo_list):
        self.tasks.append(input("Enter a new task: "))
        print_todo_list() 

    def remove_task_from_list():
        pass

    def show_list_of_tasks():
        pass

    def clear_all_tasks_from_list():
        pass 
