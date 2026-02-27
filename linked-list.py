''' Methods to include:
* Append: Adds the given element to the end of the list
* Remove: Traveses the list for the given element, and then removes it from the list
* Contains: Traverses the list for the given element, and returns it if it exists.
* Size: Returns the length of the list
* Readout: Returns a list readout of every element in the linked list.
'''

class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.nextnode = None

class LinkedList:
    def __init__(self):
        self.root =  None
        self.tail = None
        self.size = 0

    def append(self, value):
        if self.root == None:
            self.root = LinkedListNode(value)
            self.tail = self.root
        else:
            self.tail.nextnode = LinkedListNode(value)
            self.tail = self.tail.nextnode
        self.size += 1

    def readout(self):
        cursor = self.root
        print_list = []
        while (cursor != None):
            print_list.append(cursor.value)
            cursor = cursor.nextnode
        print(print_list)

    def contains(self, value):
        cursor = self.root
        while(cursor != None):
            if cursor.value == value:
                return True
            cursor = cursor.nextnode
        return False

    def list_size(self):
        return self.size

    def remove(self, value):
        cursor = self.root
        if cursor.value == value:
            self.root = cursor.nextnode
            return value
        while(cursor.nextnode != None):
            if cursor.nextnode.value == value:
                cursor.nextnode = cursor.nextnode.nextnode
                return value
            else:
                cursor = cursor.nextnode
        return(KeyError("Couldn't find value"))




