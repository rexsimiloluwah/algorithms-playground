class Node:
    def __init__(self, data:any, link=None):
        self.data = data 
        self.link = link
        
class SinglyLinkedList:
    def __init__(self, head:Node=None, size:int=0):
        self.head = head 
        self.size = size 
        
    def size(self):
        return self.size 
        
    def insert(self, element:any) -> None:
        ''' Insert a new element at the end of a linked list '''
        node = Node(element)
        if(self.size == 0):
            self.head = node
            self.size += 1
            return       
        
        ptr = self.head
        for i in range(self.size):
            if(ptr.link != None):
                ptr = ptr.link
                
        ptr.link = node 
        self.size+=1
        
    def get_at(self, pos:int) -> any:
        ''' Get the element at a specific position in a linked list '''
        if pos == 0:
            return self.head
        if pos > self.size-1:
            return None
        ptr = self.head 
        for i in range(pos):
            ptr = ptr.link 
        return ptr
        
    def insert_at(self, pos:int, element:any) -> None:
        ''' Insert a new element at a specific position of a linked list ''' 
        node = Node(element)
        ptr = self.head
        if(pos == 0):
            self.head = node 
            self.head.link = ptr
            self.size+=1
            return
        print(self.get_at(pos-1).data)
        prev_node = self.get_at(pos-1)
        next_node = self.get_at(pos)
        prev_node.link = node 
        node.link = next_node
        self.size+=1
        
    def delete_at(self, pos:int) -> None:
        ''' Delete an element at a particular position '''
        ptr = self.head 
        if pos == 0:
            self.head = ptr.link
        prev_node = self.get_at(pos-1)
        next_node = self.get_at(pos+1)
        prev_node.link = next_node
        
    def search(self, element:any) -> int:
        ''' Returns the position of an element in the linked list '''
        ptr = self.head
        for i in range(self.size-1):
            if ptr.data == element:
                return i 
            ptr = ptr.link
        return None
        
    def reverse(self) -> None:
        ''' Reverse a singly linked list '''
        current_head = self.head 
        prev_head = None
        while current_head != None:
            next_head = current_head.link 
            current_head.link = prev_head
            prev_head = current_head 
            current_head = next_head
        self.head = prev_head
        
    def to_array(self) -> list:
        ''' Converts a linked list to an array ''' 
        ptr = self.head 
        arr = []
        while ptr != None:
            arr.append(ptr.data)
            ptr = ptr.link
            
        return arr
if __name__ == '__main__':
    l = SinglyLinkedList()
    for i in range(10):
        l.insert(i)
    print(l.to_array())
    print(l.get_at(3).data)
    l.insert_at(5, 28)
    l.delete_at(10)
    print(l.to_array())
    print(l.search(50))
    l.reverse()
    print(l.to_array())
