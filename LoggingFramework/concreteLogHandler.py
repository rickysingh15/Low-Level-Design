from handler import Handler
from log import Log
from logLevel import LogLevel
from outputStrategy import OutputStrategy

class DebugLogHandler(Handler):

    def __init__(self, output_strategies: list[OutputStrategy] = None):
        self.next = None
        self.output_strategies = output_strategies or []

    def get_next(self):
        return self.next

    def set_next(self, handler: Handler):
        self.next = handler

    def can_handle(self, log: Log):
        if log.level == LogLevel.DEBUG.value:
            self.handle(log)
        else:
            if self.next:
                self.next.can_handle(log)

    def handle(self, log: Log):
        for strategy in self.output_strategies:
            strategy.output(log)


class InfoLogHandler(Handler):

    def __init__(self, output_strategies: list[OutputStrategy] = None):
        self.next = None
        self.output_strategies = output_strategies or []

    def get_next(self):
        return self.next

    def set_next(self, handler: Handler):
        self.next = handler

    def can_handle(self, log: Log):
        if log.level == LogLevel.INFO.value:
            self.handle(log)
        else:
            if self.next:
                self.next.can_handle(log)

    def handle(self, log: Log):
        for strategy in self.output_strategies:
            strategy.output(log)


class WarningLogHandler(Handler):

    def __init__(self, output_strategies: list[OutputStrategy] = None):
        self.next = None
        self.output_strategies = output_strategies or []

    def get_next(self):
        return self.next

    def set_next(self, handler: Handler):
        self.next = handler

    def can_handle(self, log: Log):
        if log.level == LogLevel.WARNING.value:
            self.handle(log)
        else:
            if self.next:
                self.next.can_handle(log)

    def handle(self, log: Log):
        for strategy in self.output_strategies:
            strategy.output(log)


class ErrorLogHandler(Handler):

    def __init__(self, output_strategies: list[OutputStrategy] = None):
        self.next = None
        self.output_strategies = output_strategies or []

    def get_next(self):
        return self.next

    def set_next(self, handler: Handler):
        self.next = handler

    def can_handle(self, log: Log):
        if log.level == LogLevel.ERROR.value:
            self.handle(log)
        else:
            if self.next:
                self.next.can_handle(log)

    def handle(self, log: Log):
        for strategy in self.output_strategies:
            strategy.output(log)


class FatalLogHandler(Handler):

    def __init__(self, output_strategies: list[OutputStrategy] = None):
        self.next = None
        self.output_strategies = output_strategies or []

    def get_next(self):
        return self.next

    def set_next(self, handler: Handler):
        self.next = handler

    def can_handle(self, log: Log):
        if log.level == LogLevel.FATAL.value:
            self.handle(log)
        else:
            if self.next:
                self.next.can_handle(log)

    def handle(self, log: Log):
        for strategy in self.output_strategies:
            strategy.output(log)
