class EmptyQueueError(Exception):
    pass

class Queue:
    def __init__(self, data:list = []):
        """
            Args:
                arr[list] => List containing different elements (The list)
        """
        self.data = data
        self.size = len(data)

    def is_empty(self):
        return self.size == 0

    def enqueue(self, el:any) -> None:
        if not isinstance(el, list):
            self.data.append(el)
            self.size+= 1
            return
        self.data.extend(el)
        self.size+=len(el)

    def dequeue(self) -> any:
        if self.is_empty():
            raise EmptyQueueError("The Queue is currently empty [] !")

        dequeued_el = self.data[0]
        self.data = self.data[1:]
        self.size -= 1
        return dequeued_el

    def length(self) -> int:
        return self.size 

    def peek(self) -> any:
        return self.data[0]

if __name__ == '__main__':
    queue = Queue([1,4,6])
    print(queue.size)
    queue.enqueue([10,9,2])
    print(queue.dequeue())
    print(queue.length())
    print(queue.data)