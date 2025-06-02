from src.stack import Stack
import pytest


class TestStack: 

    def test_push(self):
       # Arrange 
        stc = Stack()  # []
       
        assert stc.is_empty() == True

        stc.push(-10)
        stc.push(20)
        stc.push(30)
        stc.push(420)
        stc.push(450)
        stc.push(500)
        stc.push(1000)
                 
        # Actions and Assertions
        assert stc.get_peek() == 1000
        assert stc.get_stack_size() == 7
        assert stc.get_current_stack() == [-10,20,30,420,450,500,1000]
        assert stc.is_empty() == False
        assert stc.containse(1000) == True
        assert stc.containse(230) == False


    def test_pop(self):
        stc = Stack()
        assert stc.is_empty() == True

        stc.push(-10)
        stc.push(20)
        stc.push(30)
        stc.push(420)
        stc.push(450)
        stc.push(500)
        stc.push(1000)
                 
        # Actions and Assertions
        assert stc.get_peek() == 1000
        assert stc.get_stack_size() == 7
        assert stc.get_current_stack() == [-10,20,30,420,450,500,1000]
        assert stc.is_empty() == False
        assert stc.containse(1000) == True
        assert stc.containse(230) == False

        assert stc.pop() == 1000
        assert stc.get_peek() == 500
        assert stc.get_stack_size() == 6
        assert stc.get_current_stack() == [-10,20,30,420,450,500]
        assert stc.containse(1000) == False
        

