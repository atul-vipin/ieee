stack = {"data": [], "min_stack": [], "max_stack": []}  # Dictionary-based stack initialization

# Function to push an element onto the stack
def push(s, x):
    s["data"].append(x)  # Add element to the main stack
    
    # Maintain min stack
    if not s["min_stack"] or x <= s["min_stack"][-1]:
        s["min_stack"].append(x)
    
    # Maintain max stack
    if not s["max_stack"] or x >= s["max_stack"][-1]:
        s["max_stack"].append(x)

# Function to remove the top element from the stack
def pop(s):
    if not s["data"]:
        return None  # Stack is empty
    top = s["data"].pop()  # Remove the top element
    
    # Update min stack
    if top == s["min_stack"][-1]:
        s["min_stack"].pop()
    
    # Update max stack
    if top == s["max_stack"][-1]:
        s["max_stack"].pop()
    
    return top

# Function to return the top element without removing it
def top(s):
    return s["data"][-1] if s["data"] else None  # Return the last element

# Function to get the minimum element in the stack
def getMin(s):
    return s["min_stack"][-1] if s["min_stack"] else None  # Return the last element in min stack

# Function to get the maximum element in the stack
def getMax(s):
    return s["max_stack"][-1] if s["max_stack"] else None  # Return the last element in max stack

# Usage Example
push(stack, 10)
push(stack, 20)
push(stack, 5)
push(stack, 30)
print("Top:", top(stack))  # Expected: 30
print("Min:", getMin(stack))  # Expected: 5
print("Max:", getMax(stack))  # Expected: 30
pop(stack)
print("Top after pop:", top(stack))  # Expected: 5
print("Min after pop:", getMin(stack))  # Expected: 5
print("Max after pop:", getMax(stack))  # Expected: 20
