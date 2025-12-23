
from uuid import uuid4
from task import Task
class TaskList:

    def __init__(self, name: str, tasks: list[Task] = None):
        self.id = str(uuid4())
        self.name = name
        self.tasks = tasks or []

    def get_task(self, task_id: str):
        for task in self.tasks:
            if task.id == task_id:
                return task
        print("Task with id ", task_id, " not found")
        return None
    
    def add_task(self, task: Task):
        self.tasks.append(task)

    def delete_task(self, task_id: str):
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)