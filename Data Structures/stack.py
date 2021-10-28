class Stack:
    def __init__(self, arr = []):
        """
            Args:
                arr (list) => List containing different elements (The stack)
        """
        self.data = arr
        self.size = len(arr)

    def push(self, el):

        if not isinstance(el, list):
            self.arr.append(el)

        self.arr.extend(el)
        return 

    def pop(self):
        if len(self.arr) < 1:
            raise ValueError("The Stack is currently empty [] !")

        self.arr = 
        popped_el = self.arr.pop()
        return popped_el

    def size(self):
        return f"The size of the Stack is {len(self.arr)}"


if __name__ == "__main__":
    stack = Stack([])
    stack.push([5,6,7])
    print(stack.pop())
