"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        # wrap value into a node
        new_node = ListNode(value)

        # increase length
        self.length += 1

        # if we have an item already
        if self.head:
            # set the next of the node to the current head
            new_node.next = self.head
            # change the prev of current head to new node
            self.head.prev = new_node
            # insert the new node as head
            self.head = new_node
        else:
            # in a list of 1, a single node is both
            self.head = new_node
            self.tail = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        # set the value to return
        value = self.head.value
        # run our delete method which has checks
        self.delete(self.head)
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        new_node = ListNode(value)

        self.length += 1

        # if we have a tail
        if self.tail:
            # set the current tail next to new node
            self.tail.next = new_node
            # set the new node prev to tail
            new_node.prev = self.tail
            # replace the tail
            self.tail = new_node
        else:
            # if there is no tail there is also no head
            self.head = new_node
            self.tail = new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        self.delete(node)
        self.add_to_head(node.value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node.value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        # if there is no head, there is no items, do nothing
        if not self.head:
            return

        # decrease our length since we are removing something
        self.length -= 1

        # if the head is the same as the tail, there is 1 item
        # in the list
        if self.head == self.tail:
            self.head = None
            self.tail = None

        # if the node is the head, there should be other items
        if node == self.head:
            self.head = node.next
            self.head.prev = None

        # if the node is the tail, there should be other items
        if node == self.tail:
            self.tail = node.prev
            self.tail.next = None

        else:
            value = node.value
            node.delete()
            return value

    """Returns the highest value currently in the list"""

    def get_max(self):
        if self.head == self.tail:
            return self.head.value

        node = self.head
        incr = 0
        value = 0

        while incr < self.length:
            incr += 1
            if value < node.value:
                value = node.value
            node = node.next

        return value
