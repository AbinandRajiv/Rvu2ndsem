class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = DoublyNode(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete_node(self, data):
        if self.head is None:
            print("List is empty.")
            return

        current = self.head
        while current:
            if current.data == data:  
                if current == self.head:
                    self.head = current.next
                    if self.head: 
                        self.head.prev = None
                else:
                    
                    if current.prev:
                        current.prev.next = current.next
                    if current.next:
                        current.next.prev = current.prev
                print(f"Node with data {data} deleted.")
                return
            current = current.next

        
        print(f"Node with data {data} not found.")

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")


if __name__ == "__main__":
    dll = DoublyLinkedList()

    dll.insert_at_beginning(10)
    dll.insert_at_beginning(20)
    dll.insert_at_beginning(30)

    print("Initial List:")
    dll.print_list()  

    dll.delete_node(20)
    print("\nList after deleting node with data 20:")
    dll.print_list() 

    dll.delete_node(50)  

