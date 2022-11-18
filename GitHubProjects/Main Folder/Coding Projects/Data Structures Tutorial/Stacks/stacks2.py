class Stack():

    def __init__(self):
        self.stack = list()
        
    def push(self, item):
        self.stack.append(item)