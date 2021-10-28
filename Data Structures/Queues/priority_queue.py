class EmptyQueueError(Exception):
    pass 

class Node:
    def __init__(self, data:any, priority:int):
        self.priority= priority
        self.link = None 
        self.data = data

class PriorityQueue:
    """ A priority queue is a linear data structure similar to a queue, 
        however the elements of a PQ have a priority associated with them. """
    def __init__(self, front:Node=None):
        self.front = front 
        self.size = 0
    
    def length(self) -> int:
        return self.size 

    def is_empty(self) -> bool:
        return self.size == 0 

    def enqueue(self, data:any, priority:int) -> None:
        """ Insert a new node to the priority queue based on associated priority """
        new_node = Node(data, priority)
        if self.front == None:
            self.front = new_node 
            self.size += 1
            return 
        
        ptr = self.front 
        while ptr.link and ptr.link.priority <= priority:
            ptr = ptr.link 
        temp = ptr.link 
        ptr.link, new_node.link = new_node, temp 
        self.size += 1

    def dequeue(self) -> Node:
        """ Removes element with the highest priority from the queue and returns it """
        if self.is_empty():
            raise EmptyQueueError("Queue is empty!")
        dequeued_node = self.front
        self.front = self.front.link 
        self.size -= 1
        return dequeued_node

    def peek(self) -> any:
        if self.is_empty():
            raise EmptyQueueError("Queue is empty!")
        return self.front.data 

    def display(self) -> list:
        arr = []
        if self.is_empty():
            raise EmptyQueueError("Queue is empty!")
        ptr = self.front 
        while ptr != None:
            arr.append(ptr.data)
            ptr = ptr.link 
        return arr

if __name__ == "__main__":
    q = PriorityQueue()
    print(q.size)
    q.enqueue(30,1)
    q.enqueue(45,2)
    q.enqueue(23,1)
    q.enqueue(40, 2)
    q.enqueue(90, 5)
    q.enqueue(20, 3)
    q.enqueue(100, 0)
    print(q.size)
    print(q.dequeue())
    print(q.length())
    print(q.display())

    q2 = PriorityQueue()
    #q2.dequeue()