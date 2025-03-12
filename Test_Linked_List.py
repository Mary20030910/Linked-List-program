class Linked_List:
    
    class Node:
        
        def __init__(self, val):
            # Declare and initialize the public attributes for objects of the
            # Node class. TODO replace pass with your implementation
            self.val = val
            self.next = None
            self.previous = None

    def __init__(self):
        # Declare and initialize the private attributes for objects of the
        # sentineled Linked_List class TODO replace pass with your
        # implementation
        self._head = Linked_List.Node(None)
        self._tail = Linked_List.Node(None)
        self._head.next = self._tail
        self._tail.previous = self._head
        self._size = 0

    def __len__(self):
        # Return the number of value-containing nodes in this list. TODO replace
        # pass with your implementation
        return self._size

    def append_element(self, val):
        # Increase the size of the list by one, and add a node containing val at
        # the new tail position. this is the only way to add items at the tail
        # position. TODO replace pass with your implementation
        newest = Linked_List.Node(val)
        if self._head.next is None:
            self._head.next = newest
            newest.previous = self._head
        else: 
            self._tail.previous.next = newest
            newest.next = self._tail
            newest.previous = self._tail.previous
            self._tail.previous = newest
            self._size = self._size +1




    def insert_element_at(self, val, index):
        # Assuming the head position (not the header node) is indexed 0, add a
        # node containing val at the specified index. If the index is not a
        # valid position within the list, raise an IndexError exception. This
        # method cannot be used to add an item at the tail position. TODO
        # replace pass with your implementation
        if index >= self._size or index <0:
            raise IndexError
        newest = Linked_List.Node(val)
        if index == 0:
            newest.next = self._head.next
            self._head.next.previous = newest
            self._head.next = newest
            newest.previous = self._head
            self._size = self._size + 1
            return
        else:
            current = self._head.next
            for i in range(index-1):
                current = current.next
            newest.next = current.next
            current.next.previous = newest
            newest.previous = current
            current.next = newest
            self._size = self._size +1

            

    def remove_element_at(self, index):
        # Assuming the head position (not the header node) is indexed 0, remove
        # and return the value stored in the node at the specified index. If the
        # index is invalid, raise an IndexError exception. TODO replace pass
        # with your implementation
        if index >= self._size or index<0:
            raise IndexError
        value = self.get_element_at(index)
        if index == 0:
            if self._size == 1:
                self._head.next = self._tail
                self._tail.previous = self._head
                self._size = self._size-1
            else:
                self._head.next = self._head.next.next
                self._head.next.pervious = self._head
                self._size = self._size-1
        elif index == self._size -1:
            if self._size == 1:
                self._head.next = self._tail
                self._tail.previous = self._head
                self._size = self._size-1
            else:
                self._tail.previous = self._tail.previous.previous
                self._tail.previous.next = self._tail
                self._size = self._size-1
        else:
            current = self._head.next
            for i in range(1,index):
                current = current.next
            current.next = current.next.next
            current.next.previous = current
            self._size = self._size -1
        return value



    def get_element_at(self, index):
        # Assuming the head position (not the header node) is indexed 0, return
        # the value stored in the node at the specified index, but do not unlink
        # it from the list. If the specified index is invalid, raise an
        # IndexError exception. TODO replace pass with your implementation
        if index >= self._size or index<0:
            raise IndexError
        current = self._head.next
        for i in range(index):
            current = current.next
        return current.val

    def rotate_left(self):
        # Rotate the list left one position. Conceptual indices should all
        # decrease by one, except for the head, which should become the tail.
        # For example, if the list is [ 5, 7, 9, -4 ], this method should alter
        # it to [ 7, 9, -4, 5 ]. This method should modify the list in place and
        # must not return a value. TODO replace pass with your implementation.
        if self._size == 0 or self._size == 1:
            return
        else:
            HeadVal = self._head.next.val
            self._head.next = self._head.next.next
            self._head.next.previous = self._head
            self._size = self._size-1
            self.append_element(HeadVal)

        
    def __str__(self):
        # Return a string representation of the list's contents. An empty list
        # should appear as [ ]. A list with one element should appear as [ 5 ].
        # A list with two elements should appear as [ 5, 7 ]. You may assume
        # that the values stored inside of the node objects implement the
        # __str__() method, so you call str(val_object) on them to get their
        # string representations. TODO replace pass with your implementation
        if self._size == 0:
            return "[ ]"
        else:
            current = self._head.next
            list = str(current.val)
            for k in range(self._size-1):
                current = current.next
                list = list + ", " + str(current.val)
            return "[ " + list + " ]"

    def __iter__(self):
        # Initialize a new attribute for walking through your list TODO insert
        # your initialization code before the return statement. Do not modify
        # the return statement.
        self._iter = self._head.next
        self._iter_index = 0
        return self

    def __next__(self):
        # Using the attribute that you initialized in __iter__(), fetch the next
        # value and return it. If there are no more values to fetch, raise a
        # StopIteration exception. TODO replace pass with your implementation
        if self._iter_index >= self._size:
            raise StopIteration
        else:
            PrintVal = self._iter.val
            self._iter = self._iter.next
            self._iter_index  = self._iter_index +1
            return PrintVal


    def __reversed__(self):
        # Construct and return a new Linked_List object whose nodes alias the
        # same objects as the nodes in this list, but in reverse order. For a
        # Linked_List object ll, Python will automatically call this function
        # when it encounters a call to reversed(ll) in an application. If
        # print(ll) displays [ 1, 2, 3, 4, 5 ], then print(reversed(ll)) should
        # display [ 5, 4, 3, 2, 1 ]. This method does not change the state of
        # the object on which it is called. Calling print(ll) again will still
        # display [ 1, 2, 3, 4, 5 ], even after calling reversed(ll). This
        # method must operate in linear time.
        Reverse_List = Linked_List()
        current = self._tail.previous
        for i in range(0, self._size):
            Reverse_List.append_element(current.val)
            current = current.previous
        return Reverse_List


        

if __name__ == '__main__':
    # Your test code should go here. Be sure to look at cases when the list is
    # empty, when it has one element, and when it has several elements. Do the
    # indexed methods raise exceptions when given invalid indices? Do they
    # position items correctly when given valid indices? Does the string
    # representation of your list conform to the specified format? Does removing
    # an element function correctly regardless of that element's location? Does
    # a for loop iterate through your list from head to tail? Does a for loop
    # iterate through your reversed list from tail to head? Your writeup should
    # explain why you chose the test cases. Leave all test cases in your code
    # when submitting. TODO replace pass with your tests
    a = Linked_List()
    a.append_element("DATA")
    a.append_element("R")
    a.insert_element_at("S",1)
    try:
        a.remove_element_at(3)
    except IndexError:
        print(a)
        print(len(a))
