list = {"head": None, "tail": None}  # Initialize an empty doubly linked list

# Function to insert a new node at the head (beginning) of the list
def insert_at_head(l, data):
    new_node = {"data": data, "prev": None, "next": l["head"]}  # Create a new node with given data
    if not l["head"]:  # If the list is empty, set both head and tail to the new node
        l["head"] = l["tail"] = new_node
    else:
        l["head"]["prev"] = new_node  # Link the old head node back to the new node
        l["head"] = new_node  # Update the head pointer to the new node

# Function to insert a new node at the tail (end) of the list
def insert_at_tail(l, data):
    new_node = {"data": data, "prev": l["tail"], "next": None}  # Create a new node with given data
    if not l["tail"]:  # If the list is empty, set both head and tail to the new node
        l["head"] = l["tail"] = new_node
    else:
        l["tail"]["next"] = new_node  # Link the old tail node forward to the new node
        l["tail"] = new_node  # Update the tail pointer to the new node

# Function to traverse the list forward (from head to tail) and print values
def traverse_forward(l):
    temp = l["head"]  # Start from the head node
    while temp:  # Traverse until the end of the list
        print(temp["data"], end=" , ")  # Print current node's data
        temp = temp["next"]  # Move to the next node

# Function to traverse the list backward (from tail to head) and print values
def traverse_backward(l):
    temp = l["tail"]  # Start from the tail node
    while temp:  # Traverse until the start of the list
        print(temp["data"], end=" , ")  # Print current node's data
        temp = temp["prev"]  # Move to the previous node

# Usage Example
insert_at_head(list, 10)  # Insert 10 at the head
insert_at_tail(list, 20)  # Insert 20 at the tail
insert_at_tail(list, 30)  # Insert 30 at the tail
insert_at_head(list, 5)   # Insert 5 at the head

# Display the list in forward and backward order
traverse_forward(list)  # Expected output: 5 , 10 , 20 , 30
traverse_backward(list) # Expected output: 30 , 20 , 10 , 5
