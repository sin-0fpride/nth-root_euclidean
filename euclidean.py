# Function to calculate Euclidean distance in 2D using only y-coordinates
def euclidean_distance_y(y0, y1):
    # Calculate the difference between y-coordinates
    y_diff = y1 - y0  # Difference in y
    
    # Euclidean distance in 1D (since x-coordinates are ignored): |y1 - y0|
    distance = abs(y_diff)  # Absolute value of the difference
    return distance

print(euclidean_distance_y(0, 4))  # Should print 4 (distance between y=0 and y=4)