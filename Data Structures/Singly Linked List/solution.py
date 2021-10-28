class Node:
    def __init__(self, data:int):
        self.data = data 
        self.link = None 

class SinglyLinkedList:
    def __init__(self):
        self.head = None 
        self.size = 0 

    def is_empty(self) -> bool:
        return self.size == 0 

    def length(self) -> int:
        return self.size 

    def insert(self, data:int) -> None:
        """ Inserts a new node at the end of the linked list """
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node 
            self.size += 1
            return 
        ptr = self.head 
        i = 0
        while i < self.size-1:
            ptr = ptr.link 
            i += 1
        ptr.link = new_node 
        self.size += 1 

    def get_at(self, pos:int) -> Node:
        """ Returns the node at a specific position in the linked list """
        if pos > self.size-1:
            raise Exception("Index not found in linked list.")

        if pos == 0:
            return self.head 
        
        ptr = self.head
        i = 0
        while i < pos:
            ptr = ptr.link 
            i += 1
        return ptr 

    def insert_at(self, data:int, pos:int) -> None:
        """ Inserts a new node at a specific position in the linked list """
        new_node = Node(data)
        if pos > self.size-1:
            raise Exception("Index not found in linked list.")
        ptr = self.head
        if pos == 0:
            self.head = new_node 
            new_node.link = ptr 
            self.size += 1 
            return 
        
        prev_node = self.get_at(pos-1)
        next_node = self.get_at(pos)
        prev_node.link = new_node 
        new_node.link = next_node 
        self.size += 1

    def search(self, data:int) -> int:
        """ Returns the position of an element in a linked list """
        i = 0
        ptr = self.head 
        while i < self.size:
            if ptr.data == data:
                return i 
            ptr = ptr.link 
            i += 1 
        return -1
        
    def delete_at(self, pos:int) -> None:
        """ Deletes the element at a specific position in a linked list """
        if pos > self.size - 1:
            raise Exception("Index not found in linked list.")

        if pos == 0:
            self.head = self.head.link
            self.size -= 1 
            return 

        prev_node = self.get_at(pos-1)
        next_node = self.get_at(pos+1)
        prev_node.link = next_node 
        self.size -= 1

    def delete_data(self, data:int) -> None:
        """ Deletes a specific element from the linked list """
        pos = self.search(data)
        if pos == -1:
            raise Exception("Element not found in linked list.")
        self.delete_at(pos) 

    def reverse(self) -> None:
        """ Reverses a singly linked list """
        prev_node = None 
        current_node = self.head 
        while current_node:
            next_node = current_node.link 
            current_node.link = prev_node 
            prev_node = current_node 
            current_node = next_node 
        self.head = prev_node

    def display(self) -> None:
        """ Displays a linked list in array format """
        arr = []
        ptr = self.head
        for i in range(self.size):
            arr.append(ptr.data)
            ptr = ptr.link 
        
        print("Linked list: ", arr)

if __name__ == '__main__':
    l = SinglyLinkedList()
    for i in range(10):
        l.insert(i)
    l.insert_at(28, 5)
    print(l.search(28))
    print(l.search(50))
    #print(l.get_at(12).data)
    l.delete_data(28)
    l.delete_at(1)
    l.display()
    l.reverse()
    l.display()