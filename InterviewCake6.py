import pytest

# Returns a rectangle of intersection if there
# is an intersection. This includes returning an 
# edge with either a width or length of 0 if  that
# is the only intersection.
def find_intersection(rec1, rec2):
    
    intersection = {}
    
    # Let's find the left x and width of the intersection
    if (rec1['left_x'] <= rec2['left_x'] <= rec1['left_x'] + rec1['width']):
        intersection['left_x'] = rec2['left_x']
        x_intersected = True
    elif (rec2['left_x'] <= rec1['left_x'] <= rec2['left_x'] + rec2['width']):
        intersection['left_x'] = rec1['left_x']
        x_intersected = True
    else:
       intersection['left_x'] = None
       intersection['width'] = None
       x_intersected = False

    if (x_intersected):
        intersection['width'] = min(
            rec1['left_x'] + rec1['width'], 
            rec2['left_x'] + rec2['width']) 
        intersection['width'] -= intersection['left_x']

    # Let's find the bottom y and height of the intersection
    if (rec1['bottom_y'] <= rec2['bottom_y'] <= rec1['bottom_y'] + rec1['height']):
        intersection['bottom_y'] = rec2['bottom_y']
        y_intersected = True
    elif (rec2['bottom_y'] <= rec1['bottom_y'] <= rec2['bottom_y'] + rec2['height ']):
        intersection['bottom_y'] = rec2['bottom_y']
        y_intersected = True
    else:
       intersection['bottom_y'] = None
       intersection['height'] = None
       y_intersected = False

    if (y_intersected):
        intersection['height'] = min(
            rec1['bottom_y'] + rec1['height'], 
            rec2['bottom_y'] + rec2['height']) 
        intersection['height'] -= intersection['bottom_y']

    return intersection

# Case with no intersection
rec = find_intersection({'left_x': 0, 'width': 1, 'bottom_y': 0, 'height': 1}, 
    {'left_x': 5, 'width': 1, 'bottom_y': 5, 'height': 1})

assert rec['left_x'] == None and rec['width'] == None
assert rec['bottom_y'] == None and rec['height'] == None

# Case with a simple intersection 
rec = find_intersection({'left_x': 0, 'width': 5, 'bottom_y': 0, 'height': 5}, 
    {'left_x': 3, 'width': 7,'bottom_y': 3, 'height': 7})

assert rec['left_x'] == 3 and rec['width'] == 2
assert rec['bottom_y'] == 3 and rec['height'] == 2

# Case where one rectangle is completely inside another
rec = find_intersection({'left_x': 0, 'width': 5, 'bottom_y': 0, 'height': 5}, 
    {'left_x': 2, 'width': 1,'bottom_y': 2, 'height': 1})

assert rec['left_x'] == 2 and rec['width'] == 1
assert rec['bottom_y'] == 2 and rec['height'] == 1

# Case with an intersection on a vertical edge 
rec = find_intersection({'left_x': 0, 'width': 5, 'bottom_y': 0, 'height': 5}, 
    {'left_x': 5, 'width': 7,'bottom_y': 0, 'height': 7})

assert rec['left_x'] == 5 and rec['width'] == 0
assert rec['bottom_y'] == 0 and rec['height'] == 5

# Case with an intersection on a horizontal edge
rec = find_intersection({'left_x': 0, 'width': 5, 'bottom_y': 0, 'height': 5}, 
    {'left_x': 0, 'width': 7,'bottom_y': 5, 'height': 7})

assert rec['left_x'] == 0 and rec['width'] == 5
assert rec['bottom_y'] == 5 and rec['height'] == 0
