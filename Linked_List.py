class Linked_List:
    
    class Node:
        
        def __init__(self, val):
            # Declare and initialize the public attributes for objects of the
            # Node class. TODO replace pass with your implementation
            self.val = val # initiate public self linked_list
            self.next = None
            self.previous = None

    def __init__(self):
        # Declare and initialize the private attributes for objects of the
        # sentineled Linked_List class TODO replace pass with your
        # implementation
        self._head = Linked_List.Node(None) # initiate private self linked_list 
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
        if self._head.next is None: # when there's no node in the self linked_list, append the element after the head
            self._head.next = newest
            newest.previous = self._head
        else: 
            self._tail.previous.next = newest # otherwise, append the element before the tail 
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
        if index >= self._size or index <0: # when the index number is equal,  greater than the self.size  or smaller than the self.size, it is invalid index
            raise IndexError                
        newest = Linked_List.Node(val)
        if index == 0:  # when the index is 0, which means insert right after the head
            newest.next = self._head.next
            self._head.next.previous = newest
            self._head.next = newest
            newest.previous = self._head
            self._size = self._size + 1
            return
        else:   # otherwise, need to loop the linked_list to find the index position, and than insert. 
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
        if index >= self._size or index<0: # when the index number is equal,  greater than the self.size  or smaller than the self.size, it is invalid index
            raise IndexError
        value = self._head.next.val # save the value after the self._head
        if index == 0: # for index 0, it is just delete the node right after the self._head
            if self._size == 1:    # if self._size is one, when the only node is deleted, just link the head and tail. 
                self._head.next = self._tail
                self._tail.previous = self._head
                self._size = self._size-1
            else:   # other wise, link the head with the node after node need to remove
                self._head.next = self._head.next.next
                self._head.next.pervious = self._head
                self._size = self._size-1
        elif index == self._size -1: #remove the node before the tail
            value = self._tail.previous.val
            if self._size == 1:     # if self._size is one, when the only node is deleted, just link the head and tail. 
                self._head.next = self._tail
                self._tail.previous = self._head
                self._size = self._size-1
            else:
                self._tail.previous = self._tail.previous.previous # other wise just link the nodes before node need to be removed and the tail
                self._tail.previous.next = self._tail
                self._size = self._size-1
        else:
            current = self._head.next # for general case, we need to loop the self linked_list to find the place to remove the node and then remove it. 
            for i in range(1,index):
                current = current.next
            value = current.next.val
            current.next = current.next.next
            current.next.previous = current
            self._size = self._size -1
        return value



    def get_element_at(self, index):
        # Assuming the head position (not the header node) is indexed 0, return
        # the value stored in the node at the specified index, but do not unlink
        # it from the list. If the specified index is invalid, raise an
        # IndexError exception. TODO replace pass with your implementation
        if index >= self._size or index<0: # when the index number is equal,  greater than the self.size  or smaller than the self.size, it is invalid index
            raise IndexError
        current = self._head.next    
        for i in range(index):  #use for loop to find the place we want to get the element. 
            current = current.next
        return current.val

    def rotate_left(self):
        # Rotate the list left one position. Conceptual indices should all
        # decrease by one, except for the head, which should become the tail.
        # For example, if the list is [ 5, 7, 9, -4 ], this method should alter
        # it to [ 7, 9, -4, 5 ]. This method should modify the list in place and
        # must not return a value. TODO replace pass with your implementation.
        if self._size == 0 or self._size == 1: #if the size is 0 and 1, rotate_left can not change anything
            return
        else:
            HeadVal = self._head.next.val #save the node after head value
            self._head.next = self._head.next.next #link the head to the second one so move the whole linked list except the first to the left
            self._head.next.previous = self._head # through this way, we need to delete the size because we delete the node after the head
            self._size = self._size-1
            self.append_element(HeadVal) # then append the saved value and it will increase size by one 

        
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
    test_code = Linked_List()
    print("Test empty list")
    print("Test: If the len method return correct size")
    try:
        print(len(test_code))
    except IndexError:
        print("Error:Index out of bound")

    print("Test appending method")
    try:
        test_code.append_element(3)
        print(test_code._tail.previous.val)
    except IndexError:
        print("Error:Index out of bound")
    test_code.remove_element_at(0)

    print("\n")
    print("Test: Insert at index 0: should return error")
    try:
        test_code.insert_element_at(10,0)
    except IndexError:
        print("Error:Index out of bound")
    print("Test: Insert at positive index: should return error")
    try:
        test_code.insert_element_at(10,3)
    except IndexError:
        print("Error:Index out of bound")
    print("Test: Insert at negative index: should return error")
    try:
        test_code.insert_element_at(10,-3)
    except IndexError:
        print("Error:Invalid Index")
    

    print("\n")
    print("Test remove method at index 0: should return error")
    try:
        test_code.remove_element_at(0)
    except IndexError:
        print("Error: Index out of bound")
    print("Test remove method at negative index: should return error")
    try:
        test_code.remove_element_at(-1)
    except IndexError:
        print("Error: Invalid Index")
    print("Test remove method at positive Index: should return error")
    try:
        test_code.remove_element_at(3)
    except IndexError:
        print("Error: Index out of bound")
    print("\n")

    print("Test: get_element_at index 0: should return error")
    try:
        test_code.get_element_at(0)
    except IndexError:
        print("Error: Index out of bound")
    print("Test:Get_element_at positive index: should return error")
    try:
        test_code.get_element_at(5)
    except IndexError:
        print("Error: Index out of bound")
    print("Test:Get_element_at negative index: should return error")
    try:
        test_code.get_element_at(-10)
    except IndexError:
        print("Error:Index out of bound")
    print("\n")
    
    print("Test: rotate when it is an empty list, it should return as []")
    try:
        test_code.rotate_left()
        print(str(test_code))
    except IndexError:
        print("Error:Index out of bound")
    
    print("\n")
    print("Test linked list has multiple variables inside the list：")
    print("First append several numbers into the list")
    try:
        test_code.append_element(1)
        test_code.append_element(2)
        test_code.append_element(3)
        test_code.append_element(4)
    except IndexError:
        print("Error:Out of bound")
    print("Test: if len method return correct list size, here it should return 4:")
    try:
        print(len(test_code))
    except IndexError:
        print("Error:Out of bound")
    print("Now the linked list is:"+str(test_code))
    print("Test: if len method return correct list size, here it should return 4:")
    try:
        print(len(test_code))
    except IndexError:
        print("Error:Out of bound")
    print("Test:Insert at index 0: should return with size+1 and insert element after head")
    try:
        test_code.insert_element_at(10,0)
    except IndexError:
        print("Error:Out of Bound")
    print("After insert at index 0:"+str(test_code))
    print("Test:Insert at positive index but smaller than self._size-1: should return with size+1 and insert element after the index place")
    try:
        test_code.insert_element_at(20,3)
    except IndexError:
        print("Error:Out of Bound")
    print("After insert at index 3 which is smaller than the self_size:"+str(test_code))
    print("Test:Insert at index >= self._size: should return error")
    try:
        test_code.insert_element_at(30,6)
    except IndexError:
        print("Error:Out of Bound")
    print("Test:Insert at negative index: should return error")
    try:
        test_code.insert_element_at(30,-5)
    except IndexError:
        print("Error:Invalid Index")
    
    print("\n")
    print("Test:Remove at index equals to self.size: should return error")
    try:
        test_code.remove_element_at(6)
    except IndexError:
        print("Error:Out of Bound")
    print("Test: Remove at positive index equal to self.size-1: should return size-1 and remove the element before size_tail")
    try:
        test_code.remove_element_at(5)
    except IndexError:
        print("Error:Out of Bound")
    print("After Remove the element in the index equal to self.size-1:" + str(test_code))
    print("Test: Remove at negative index: should return error ")
    try:
        test_code.remove_element_at(-5)
    except IndexError:
        print("Error:Invalid Index")
    print("\n")
    print("Test: left rotate, when it has multiple ")
    try:
        test_code.rotate_left()
        print(test_code)
    except IndexError:
        print("Error:Out of Bound")
    print("\n")
    print("Test: for loop of the Linked List which should return every value in the Linked List")
    try:
        for val in test_code:
            print(val)
    except:
        print("Error:Out of Bound")
    print("\n")
    print("Test: for loop of the reserved Linked List which should return every value in the Linked List in reserve order")
    try:
        for val in reversed(test_code):
            print(val)
    except:
        print("Error:Out of Bound")

