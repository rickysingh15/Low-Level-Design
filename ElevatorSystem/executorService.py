
from concurrent.futures import ThreadPoolExecutor
import threading

class ExecutorService:

    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):

        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "_initialized"):
            self._initialized = True
            self.executor = ThreadPoolExecutor(max_workers=3)
            self.futures = dict()

    def start_on_thread(self, elevator, callable):
        future = self.executor.submit(callable)    
        self.futures[elevator] = future
        # print("starting callable on thread ", future, " with elevator ", elevator)
        # self.futures[elevator].exception(5)