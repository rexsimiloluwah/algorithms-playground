class Stack:

    def __init__(self, arr = []):
        """
            Args:
                arr (list) => List containing different elements (The stack)
        """
        self.arr = arr

    def push(self, el):

        if not isinstance(el, list):
            self.arr.append(el)

        self.arr.extend(el)
        return 

    def pop(self):
        if len(self.arr) < 1:
            raise ValueError("The Stack is currently empty [] !")
            return None

        popped_el = self.arr.pop()
        return popped_el

    def size(self):
        return f"The size of the Stack is {len(self.arr)}"


class Queue:

    def __init__(self, arr = []):
        """
            Args:
                arr[list] => List containing different elements (The list)
        """
        self.arr = arr

    def enqueue(self, el):

        if not isinstance(el, list):
            self.arr.append(el)

        self.arr.extend(el)

        return

    def dequeue(self):

        if len(self.arr) < 1:
            raise ValueError("The Queue is currently empty [] !")
            return None

        dequeued_el = self.arr.pop(0) # First In
        return dequeued_el

    def size(self):
        return f"The size of the Queue is {len(self.arr)}"

if __name__ == "__main__":
    stack = Stack([])
    stack.push([5,6,7])
    print(stack.pop())

    queue = Queue([1,4,6])
    queue.enqueue([10,9,2])
    print(queue.dequeue())

    print(queue.size())
    print(stack.size())
