
from taskManager import TaskManager
from userManager import UserManager
from priorityEnum import PriorityLevel
from user import User

class TaskServiceInstance:

    def __init__(self, task_manager: TaskManager, user_manager: UserManager):
        self.task_manager = task_manager
        self.user_manager = user_manager

    def create_user(self, name: str):
        return self.user_manager.create_user(name)
    
    def create_task(self, title: str, description: str, due_date: str, priority: PriorityLevel, created_by: User):
        return self.task_manager.create_task(title, description, due_date, priority, created_by)
    
    def create_task_list(self, name):
        return self.task_manager.create_task_list(name)