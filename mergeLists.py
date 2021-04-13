class Node:
    # constructor
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        # Create a new node with the parameter data for the element
        aNode = Node(data)
        # If the linked list already has values, iterate through to insert the new element
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = aNode
        # Else (if there exists no values in the linked list) set the head pointer to the new node
        else:
            self.head = aNode

    # Prints out the linked list
    def printLL(self):
        current = self.head
        print("[", end="")
        while(current):
            print(current.data, end=',')
            current = current.next
        print("]")


def merge(list1, list2):
    # Initilize temp (placeholder for the merged linked list)
    temp = None
    # If list1 is empty, then return list2 (no merging needed)
    if list1 == None:
        return list2
    # If list2 is empty, then return list1 (no merging needed)
    if list2 == None:
        return list1
    # This starts at the first element of the lists. If the first element of list1 <= list2, then add list1 to temp
    # This basically means add the lowest value (because we are creating a merged list of ascending values)
    if list1.data <= list2.data:
        temp = list1
        # Calls merge again to find the temp.next value, continue until it reaches the end
        temp.next = merge(list1.next, list2)
    # Else (list1.data > list2.data), set temp = list 2 (since list2 would have the lower value)
    # Works in the same fashion as above
    else:
        temp = list2
        temp.next = merge(list1, list2.next)
    # return the new merged list
    return temp


def main():
    L1 = SinglyLinkedList()
    L1.insert(2)
    L1.insert(4)
    L1.insert(7)
    L1.insert(13)
    L1.insert(19)
    L1.printLL()
    # Linked List of L2
    L2 = SinglyLinkedList()
    L2.insert(1)
    L2.insert(5)
    L2.insert(6)
    L2.insert(9)
    L2.insert(15)
    L2.insert(20)
    L2.printLL()
    # Merge Function
    Merged = SinglyLinkedList()
    Merged.head = merge(L1.head, L2.head)
    # Merged linked list should output: 1,2,4,5,6,7,9,13,15,19,20
    Merged.printLL()


if __name__ == "__main__":
    main()
