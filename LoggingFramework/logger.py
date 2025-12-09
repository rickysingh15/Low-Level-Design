
from message import Message
from log import Log
from logLevel import LogLevel
from outputStrategy import OutputStrategy
from handler import Handler
from concreteLogHandler import DebugLogHandler, InfoLogHandler, ErrorLogHandler, WarningLogHandler, FatalLogHandler
import threading

class Logger:

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, min_log_level: str, output_strategies:list[OutputStrategy] = None):
        if not hasattr(self, "_initialized"):
            self._initialized = True
            self.min_log_level = min_log_level
            self.strategies = output_strategies or []
            self.lock = threading.Lock()
            self.log_scores = {
                LogLevel.DEBUG.value:10,
                LogLevel.INFO.value:20,
                LogLevel.WARNING.value: 30,
                LogLevel.ERROR.value: 40,
                LogLevel.FATAL.value: 50
            }
            h1 = DebugLogHandler(self.strategies)
            h2 = InfoLogHandler(self.strategies)
            h3 = WarningLogHandler(self.strategies)
            h4 = ErrorLogHandler(self.strategies)
            h5 = FatalLogHandler(self.strategies)
            h1.set_next(h2)
            h2.set_next(h3)
            h3.set_next(h4)
            h4.set_next(h5)
            self.head_log_handler = h1

    def output(self, level: str, message: str):
        with self.lock:
            if self.check_min_level(level):
                log = Log(message=message, level=level)
                self.head_log_handler.can_handle(log)
            else:
                return

    def check_min_level(self, level: str):
        return self.log_scores.get(self.min_log_level, 10) <= self.log_scores.get(level)

    def info(self, message: str):
        level = LogLevel.INFO.value
        self.output(level, message)

    def debug(self, message: str):
        level = LogLevel.DEBUG.value
        self.output(level, message)

    def error(self, message: str):
        level = LogLevel.ERROR.value
        self.output(level, message)

    def fatal(self, message: str):
        level = LogLevel.FATAL.value
        self.output(level, message)

    def warning(self, message: str):
        level = LogLevel.WARNING.value
        self.output(level, message)

