class TaskItem:
    def __init__(self, description, deadline, status=0):
        self.description = description
        self.deadline = deadline
        self.status = status

    def set_status(self, new_status):
        self.status = new_status

    def __repr__(self):
        return (f"(description='{self.description}', "
                f"deadline='{self.deadline}', status={self.status})")

class Tasks:
    def __init__(self):
        self.tasklist = []

    def add_task(self, description, deadline, status=0):
        task = TaskItem(description, deadline, status)
        self.tasklist.append(task)

    def change_status(self, index, new_status):
        if 0 <= index < len(self.tasklist):
            self.tasklist[index].set_status(new_status)
        else:
            print("Invalid index")

    def print_tasks_with_status(self, status):
        for task in self.tasklist:
            if task.status == status:
                print(task)

    def __repr__(self):
        return "\n".join(str(task) for task in self.tasklist)

# Пример использования
task_list = Tasks()
task_list.add_task('Задача-1', '01.01.2024', 0)
task_list.add_task('Задача-2', '02.01.2024', 1)
task_list.add_task('Задача-3', '03.01.2024', 0)
task_list.add_task('Задача-4', '04.01.2024', 0)

print("Список всех задач status=0 не выполнено / status=1 выполнено:")
print(task_list)

# Изменение статуса задачи
task_list.change_status(1, 0)

print("\nСписок текущих (не выполненных) задач status=0:")
task_list.print_tasks_with_status(0)