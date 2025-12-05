import time
#Lista enlazada
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)

#Array
array = []
start = time.time()
for i in range(1000):
    array.append(i)
end = time.time()
array_time = end - start

#Prueba con lista enlazada
linked_list = LinkedList()
start = time.time()
for i in range(1000):
    linked_list.insert(i)
end = time.time()
linked_time = end - start

print("Resultados de inserción de 1000 elementos:")
print(f"- Array (list):       {array_time} segundos")
print(f"- Linked List:        {linked_time} segundos")
