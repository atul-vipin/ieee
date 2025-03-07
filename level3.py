intervals = []  # List to store merged intervals

# Function to add a new interval and merge if necessary
def addInterval(start, end):
    new_interval = [start, end]
    
    # Insert the new interval in sorted order
    i = 0
    while i < len(intervals) and intervals[i][0] < start:
        i += 1
    intervals.insert(i, new_interval)
    
    # Merge overlapping intervals
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    
    global intervals
    intervals = merged  # Update intervals with the merged result

# Function to get the current set of non-overlapping intervals
def getIntervals():
    return intervals

# Usage Example
addInterval(1, 5)
addInterval(6, 8)
addInterval(4, 7)
print(getIntervals())  # Expected output: [[1, 8]]
