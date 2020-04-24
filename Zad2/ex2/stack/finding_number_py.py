# 2. Wykorzystując dziedziczenie rozszerz klasę Stack znajdującą się w module stack
# (projekt znajduje się na Moodle w pliku ex2.zip) metodę, która pozwoli odczytać
# aktualną minimalną wartość znajdującą się na stosie. Uwaga! Nie wolno zmieniać
# implementacji klasy Stack.
from .stack import Stack


class MinMaxStack(Stack):
    def __init__(self):
        Stack.__init__(self)

    def lowest_number(self):
        lowest = self.top()
        helping_stack = Stack()
        while not self.is_empty():
            if (self.top() < lowest):
                lowest = self.top()

            x = self.top()
            helping_stack.push(x)
            y = self.pop()

        while not helping_stack.is_empty():
            self.push(helping_stack.top())
            helping_stack.pop()

        return lowest
