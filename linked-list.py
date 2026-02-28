''' Methods to include:
* Append: Adds the given element to the end of the list
* Remove: Traveses the list for the given element, and then removes it from the list
* Contains: Traverses the list for the given element, and returns it if it exists.
* Size: Returns the length of the list
* Readout: Returns a list readout of every element in the linked list.
'''
import unittest



class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.nextnode = None

class LinkedList:
    def __init__(self):
        self.head =  None
        self.tail = None
        self.size = 0

    def __getitem__(self, index):
        if index >= len(self):
            raise IndexError("Index specified larger than length of list.")
        cursor = self.head
        for i in range(index):
            cursor = cursor.nextnode
        return cursor.value

    def append(self, value):
        if self.head is None:
            self.head = LinkedListNode(value)
            self.tail = self.head
        else:
            self.tail.nextnode = LinkedListNode(value)
            self.tail = self.tail.nextnode
        self.size += 1

    def prepend(self, value):
        if self.head is None:
            self.head = LinkedListNode(value)
            self.tail = self.head
        else:
            node = LinkedListNode(value)
            node.nextnode = self.head
            self.head = node
        self.size += 1

    def readout(self):
        cursor = self.head
        print_list = []
        while (cursor is not None):
            print_list.append(cursor.value)
            cursor = cursor.nextnode
        return print_list

    def __len__(self):
        return self.size

    def remove(self, value):
        cursor = self.head
        if cursor.value == value:
            self.head = cursor.nextnode
            return value
        while(cursor.nextnode is not None):
            if cursor.nextnode.value == value:
                cursor.nextnode = cursor.nextnode.nextnode
                return value
            else:
                cursor = cursor.nextnode
        return(KeyError("Couldn't find value"))

class TestLinkedListMethods(unittest.TestCase):
    def setUp(self):
        self.link_list = LinkedList()

    def test_construction(self):
        link_list = LinkedList()
        self.assertIsInstance(link_list, LinkedList)
        self.assertEqual(len(link_list), 0)

    def test_append(self):
        self.link_list.append(1)
        self.link_list.append(2)
        self.link_list.append(3)
        self.assertEqual(self.link_list[0], 1)
        self.assertEqual(self.link_list[1], 2)
        self.assertEqual(self.link_list[2], 3)

    def test_preprend(self):
        self.link_list.prepend(1)
        self.link_list.prepend(2)
        self.link_list.prepend(3)
        self.assertEqual(self.link_list[0], 3)
        self.assertEqual(self.link_list[1], 2)
        self.assertEqual(self.link_list[2], 1)

    def test_remove(self):
        self.link_list.append(1)
        self.link_list.append(2)
        self.link_list.append(3)
        self.link_list.remove(2)
        self.assertEqual(self.link_list.readout(), [1,3])



if __name__ == '__main__':
    unittest.main()


