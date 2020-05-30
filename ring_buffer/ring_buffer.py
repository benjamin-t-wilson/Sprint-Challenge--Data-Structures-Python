from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('./doubly_linked_list')

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = DoublyLinkedList()

        # this will be used to rotate us across indexes on a full storage
        self.mru = None

    def append(self, item):
        # on our first one we will add to tail and set our most recently used
        if self.storage.length == 0:
            self.storage.add_to_tail(item)
            self.mru = self.storage.tail
            return
        
        # if we are at capacity, close our loop
        if self.storage.length == self.capacity and self.storage.tail.next is None:
            self.storage.tail.next = self.storage.head
        
        # if our loop is open, we are free to add
        if self.storage.tail.next is None:
            self.storage.add_to_tail(item)
            self.mru = self.mru.next

        # assuming our loop is closed, we can constantly just .next and change values
        else:
            self.mru = self.mru.next
            self.mru.value = item

    def get(self):
        # set a cursor past the head
        current_node = self.storage.head.next

        # start with the head's value so we don't miss it
        storage_contents = [self.storage.head.value]

        # hitting head would mean we have completed our loop
        while current_node is not self.storage.head:

            # if our loop is not closed, we will never hit head, and need to break
            # before we get an error
            if current_node is None:
                break
            storage_contents.append(current_node.value)
            current_node = current_node.next
        
        return storage_contents