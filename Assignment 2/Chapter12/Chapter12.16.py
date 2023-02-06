# 12.16 (Implement Stack using inheritance) In Listing 12.13, the Stack class is
# implemented using composition. Define a new Stack class using inheritance
# that extends list.
# Draw UML diagrams of the new class. Implement it. Write a test program that
# prompts the user to enter five strings and displays them in reverse order.

class Stack(list):
    def __init__(self, size):
        super().__init__()
        self.size = size
        self.counter = -1

    def push(self, val):
        if self.counter < self.size:
            self.append(val)
            self.counter += 1
        else:
            print("Stack is full!")

    def pop(self):
        if self.counter >= 0:
            res = self[self.counter]
            self[:] = self[:self.counter]
            self.counter -= 1
            return res
        else:
            return "Stack empty"

    def isEmpty(self):
        return self.counter < 0

    def peek(self):
        if not self.isEmpty():
            return self[self.counter]
        else:
            return "Stack empty"

s = Stack(5)
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
print(s.peek())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.peek())

