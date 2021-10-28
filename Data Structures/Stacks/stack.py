class EmptyStackError(Exception):
    pass 

class Stack:
    def __init__(self, data:list = []):
        """
            Args:
                data (list) => List containing different elements (The stack)
        """
        self.data = data
        self.size = len(data)

    def is_empty(self) -> bool:
        return self.size == 0

    def push(self, el:any) -> None:
        if not isinstance(el, list):
            self.data.append(el)
            self.size += 1

        self.data.extend(el)
        self.size += len(el)

    def pop(self) -> any:
        if self.is_empty():
            raise EmptyStackError("The Stack is currently empty [] !")
        popped_el = self.data[-1]
        self.data = self.data[:-1]
        self.size -= 1
        return popped_el

    def peek(self) -> any:
        return self.data[0]

    def length(self) -> int:
        return self.size

    def display(self) -> None:
        print(self.data)

if __name__ == "__main__":
    stack = Stack([5,6,7])
    stack.push([1,2,3])
    stack.display()
    print(stack.pop())
    print(stack.length())
    stack.display()