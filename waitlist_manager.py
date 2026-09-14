# Create a Node class to represent each customer in the waitlist
class Node:
    '''
    A class representing a node in a linked list.
    Attributes:
        name (str): The name of the customer.
        next (Node): A reference to the next node in the list.
    '''

    def __init__(self, name):
        self.name = name
        self.next = None



# Create a LinkedList class to manage the waitlist
class LinkedList:
    '''
    A class representing a linked list to manage a waitlist.
    Attributes:
        head (Node): The first node in the linked list.
    Methods:
        add_front(name): Adds a customer to the front of the waitlist.
        add_end(name): Adds a customer to the end of the waitlist.
        remove(name): Removes a customer from the waitlist by name.
        print_list(): Prints the current waitlist.
    '''

    def __init__(self):
        self.head = None

    def add_front(self, name):
        new_node = Node(name)
        new_node.next = self.head
        self.head = new_node

    def add_end(self, name):
        new_node = Node(name)

        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

        return f"{name} added to the end of the waitlist"

    def remove(self, name):
        if self.head is None:
            return f"{name} not found"

        if self.head.name == name:
            self.head = self.head.next
            return f"Removed {name} from the waitlist"

        current_node = self.head
        while current_node.next is not None:
            if current_node.next.name == name:
                current_node.next = current_node.next.next
                return f"Removed {name} from the waitlist"
            current_node = current_node.next

        return f"{name} not found"

    def print_list(self):
        if self.head is None:
            print("The waitlist is empty")
            return

        current_node = self.head
        while current_node is not None:
            print(f"- {current_node.name}")
            current_node = current_node.next


def waitlist_generator():
    # Create a new linked list instance
    waitlist = LinkedList()

    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")
        
        choice = input("Choose an option (1–5): ")
        
        if choice == "1":
            name = input("Enter customer name to add to front: ")
            # Call the add_front method
            waitlist.add_front(name)

        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            # Call the add_end method
            print(waitlist.add_end(name))

        elif choice == "3":
            name = input("Enter customer name to remove: ")
            # Call the remove method
            print(waitlist.remove(name))

        elif choice == "4":
            print("Current waitlist:")
            # Print out the entire linked list using the print_list method.
            waitlist.print_list()

        elif choice == "5":
            print("Exiting waitlist manager.")
            break
        else:
            print("Invalid option. Please choose 1–5.")

# Call the waitlist_generator function to start the program
if __name__ == "__main__":
    waitlist_generator()


'''
Design Memo: Write Your Design Memo Include a 200–300 word response in your code or in a .txt file:
- How does your list work?
- What role does the head play?
- When might a real engineer need a custom list like this?
'''

# This waitlist is implemented as a singly linked list. Each Node stores one
# customer's name and a next pointer. The next pointer either refers to the
# following Node or contains None when that customer is last in the list. The
# LinkedList object does not keep customer names directly; instead,
# it stores a head pointer to the first Node. Methods move through the list by
# starting at head and repeatedly following next pointers until they reach
# None.
#
# Adding a customer to the front is efficient because the program creates a
# new Node, points it at the current head, and makes that new Node the head.
# Adding a customer to the end requires traversal because this version does not
# store a tail pointer. It follows next pointers to the final Node and updates
# that Node's next pointer to reference the new customer. Removing a customer
# also traverses the list. When a matching Node is found, the previous Node's
# next pointer skips over it. Removing the first Node is a special case because
# head must be updated to the second Node.
#
# The head is the entry point for every list operation. If head is None, the
# waitlist is empty. If head refers to a Node, every other customer can be
# reached from it. Maintaining head correctly is especially important when the
# first customer is added or removed; otherwise, the program could lose access
# to the entire list.
#
# A real engineer may choose a custom linked list when insertions or removals
# happen often and direct references to nearby items are available. Examples
# include a task scheduler, a media playlist, a cache eviction queue, or an
# embedded system with constrained memory. In many Python applications, the
# built-in list or collections.deque is a better practical choice, but building
# this structure demonstrates how those pointer relationships work.
