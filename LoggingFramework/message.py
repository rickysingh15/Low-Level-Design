

class Message:

    def __init__(self, message: str):
        self.content = message

    def get_content(self):
        return self.content
    
    def set_content(self, message: str):
        self.message = message