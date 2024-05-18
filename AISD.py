import random
import time

# Class definition for a linked list node
class Node:
    def __init__(self, info):
        self.info = info
        self.next = None

# Function to measure time taken for creating sorted linked list
def measure_sorted_list_creation(size_list, range_val):
    times = []
    for size in size_list:
        lista = generate_random_unique_list(size, range_val)
        start_time = time.time()
        sorted_list = None
        current = lista
        for _ in range(size):
            sorted_list = insert_sorted(sorted_list, current.info)
            current = current.next
        end_time = time.time()
        times.append(end_time - start_time)
    return times

# Function to measure time taken for creating binary search tree (BST)
def measure_bst_creation(size_list, range_val):
    times = []
    for size in size_list:
        lista = generate_random_unique_list(size, range_val)
        start_time = time.time()
        root = None
        root = insert_list_elements_into_bst(lista, root)
        end_time = time.time()
        times.append(end_time - start_time)
    return times

# Function to measure time taken for searching an element in sorted linked list
def measure_search_in_sorted_list(sorted_list, keys):
    start_time = time.time()
    for key in keys:
        current = sorted_list
        while current is not None:
            if current.info == key:
                break
            current = current.next
    end_time = time.time()
    return end_time - start_time

# Function to measure time taken for searching an element in binary search tree (BST)
def measure_search_in_bst(root, keys):
    start_time = time.time()
    for key in keys:
        current = root
        while current is not None:
            if current.info == key:
                break
            elif current.info < key:
                current = current.right
            else:
                current = current.left
    end_time = time.time()
    return end_time - start_time

# Function to measure time taken for deleting elements from a sorted linked list
def measure_sorted_list_deletion(sorted_list):
    start_time = time.time()
    current = sorted_list
    while current is not None:
        temp = current
        current = current.next
        del temp
    end_time = time.time()
    return end_time - start_time

# Function to measure time taken for deleting elements from a binary search tree (BST)
def measure_bst_deletion(root):
    def delete_nodes(root):
        if root:
            root.left = delete_nodes(root.left)
            root.right = delete_nodes(root.right)
            del root
            return None

    start_time = time.time()
    root = delete_nodes(root)
    end_time = time.time()
    return end_time - start_time

# Function to insert an element into a sorted linked list
def insert_sorted(list, a):
    new_node = Node(a)

    # If the list is empty or the new node should be inserted at the beginning
    if list is None or list.info >= new_node.info:
        new_node.next = list
        list = new_node
    else:
        current = list
        # Traverse the list until the appropriate position is found
        while current.next is not None and current.next.info < new_node.info:
            current = current.next
        # Insert the new node into the list
        new_node.next = current.next
        current.next = new_node

    return list

# Function to generate a flat list of random unique natural numbers
def generate_random_unique_list(size, range2):
    unique_set = set()
    head = None
    tail = None

    for _ in range(size):
        random_data = random.randint(1, range2)
        while random_data in unique_set:
            random_data = random.randint(1, range2)
        unique_set.add(random_data)

        new_node = Node(random_data)

        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node

    return head

# Function to display the list
def display_list(head):
    current = head
    while current is not None:
        print(current.info, end=" ")
        current = current.next
    print()

# Class definition for a binary search tree node
class TreeNode:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

# Function to insert an element into a binary search tree (BST)
def insert(root, x):
    if root is None:
        return TreeNode(x)
    if root.info > x:
        root.left = insert(root.left, x)
    elif root.info < x:
        root.right = insert(root.right, x)
    return root

# Function to insert elements from the generated list into a BST
def insert_list_elements_into_bst(head, root):
    current = head
    while current is not None:
        root = insert(root, current.info)
        current = current.next
    return root

# Main function
def main():
    size_list = [5000]  # Size of the list (adjust as needed)
    range_val = max(size_list) * 10  # Range of random numbers (adjust as needed)

    # Measure time taken for creating a sorted linked list
    time_sorted_list_creation = measure_sorted_list_creation(size_list, range_val)

    # Measure time taken for creating a binary search tree (BST)
    time_bst_creation = measure_bst_creation(size_list, range_val)

    # Generate random keys for searching
    keys = [random.randint(1, range_val) for _ in range(max(size_list))]

    # Measure time taken for searching all keys in sorted list
    sorted_list = generate_random_unique_list(max(size_list), range_val)
    time_search_sorted_list = measure_search_in_sorted_list(sorted_list, keys)

    # Measure time taken for searching all keys in BST
    bst_root = insert_list_elements_into_bst(sorted_list, None)
    time_search_bst = measure_search_in_bst(bst_root, keys)

    # Measure time taken for deleting elements from sorted list
    time_sorted_list_deletion = measure_sorted_list_deletion(sorted_list)

    # Measure time taken for deleting elements from BST
    time_bst_deletion = measure_bst_deletion(bst_root)

    # Print results
    print("Time taken for creating sorted linked list:", time_sorted_list_creation)
    print("Time taken for creating binary search tree:", time_bst_creation)
    print("Time taken for searching all keys in sorted list:", time_search_sorted_list)
    print("Time taken for searching all keys in BST:", time_search_bst)
    print("Time taken for deleting elements from sorted list:", time_sorted_list_deletion)
    print("Time taken for deleting elements from BST:", time_bst_deletion)

if __name__ == "__main__":
    main()