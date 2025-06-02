
class Stack:
    def __init__(self):
        self.items=[]

    def push(self,value):
        self.items.append(value)

    def pop(self):
        popped_item = self.items.pop()
        return popped_item
    
    def get_peek(self):
        return self.items[-1] 
    
    def get_current_stack(self):
        return self.items
    
    def get_stack_size(self):
        return len(self.items)
    
    def containse(self, value):
        return self.items.__contains__(value)
    
    def is_empty(self):
        return len(self.items) == 0