
import threading
from task import Task
from taskList import TaskList
from statusEnum import StatusType
from priorityEnum import PriorityLevel
from user import User
from sortStrategy import SortStrategy, PrioritySortStrategy, DueDateSortStrategy

class TaskManager:

    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, tasks: dict[str, Task] = None, task_lists: dict[str, TaskList] = None):
        if not hasattr(self, "_initialized"):
            self.initialized = True
            self.tasks = tasks or {}
            self.task_lists = task_lists or {}

    def create_task(self, title: str, description: str, due_date: str, priority: PriorityLevel, created_by: User):
        with TaskManager._lock:
            task = Task(title, description, due_date, priority, created_by)
            self.tasks[task.id] = task
            return task

    def create_task_list(self, name: str):
        with TaskManager._lock:
            task_list = TaskList(name)
            self.task_lists[task_list.name] = task_list
            return task_list
    
    def update_task(self, task: Task, title: str = None, description: str = None, due_date: str = None, priority: PriorityLevel = None, status: StatusType = None):
        pass

    def delete_task(self, task):
        with TaskManager._lock:
            if task.id in self.tasks:
                del self.tasks[task.id]

    def assign_user_to_task(self, task: Task, user: User):
        with TaskManager._lock:
            task.assign_user(user)


    def search(self, keyword: str, sort_strategy: SortStrategy):
        resulting_tasks = []
        for task_list in self.task_lists.values():
            for task in task_list:
                key = keyword.lower()
                if key in task.title.lower() or task.description.lower():
                    resulting_tasks.append(task)
        
        sort_strategy.sort(resulting_tasks)
        return resulting_tasks
    