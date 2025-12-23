
from taskManager import TaskManager
from userManager import UserManager
from taskServiceInstance import TaskServiceInstance

class TaskManagementService:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, "initialized"):
            self.initialized = True
            self.task_manager = TaskManager()
            self.user_manager = UserManager()

    def get_service(self):
        return TaskServiceInstance(self.task_manager, self.user_manager)