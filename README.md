# fmaze
simple and easy maze


"""
[Module] In maze package
"""
import random
import turtle 


screen = turtle.getscreen()
screen.setup(width = 500, height = 500)

obstacles_list = []


# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100



# def create_obstacles():
"""
    creates the obstacles
"""

def generate_obstacles():
    """
    get obstacles:
        creates a list ob_list which creates a random x and y list,
        using the parameters given
        returns them as a list of tuples with x and y co-ordinates
    """
    global obstacles_list
    for y in range(-180,180,5):
        obstacles_list.append((-80,y))
    for x in range(-80,80,5):
        obstacles_list.append((x,180))
    for y in range(-160,185,5):
        obstacles_list.append((80,y))
    for x in range(-50,80,5):
        obstacles_list.append((x,-160))
    for y in range(-160,165,5):
        obstacles_list.append((-50,y))
    for x in range(-50,50,5):
        obstacles_list.append((x,160))
    for y in range(-140,165,5):
        obstacles_list.append((50,y))
    for x in range(-30,50,5):
        obstacles_list.append((x,-140))
    for y in range(-140,145,5):
        obstacles_list.append((-30,y))
    for x in range(-30,30,5):
        obstacles_list.append((x,140))
    for y in range(-120,145,5):
        obstacles_list.append((30,y))
    for x in range(-10,30,5):
        obstacles_list.append((x,-120))
    for y in range(-120,125,5):
        obstacles_list.append((-10,y))
    for x in range(-10,20,5):
        obstacles_list.append((x,120))
    for y in range(-120,95,5):
        obstacles_list.append((10,y))
        

    return obstacles_list 

   


def get_obstacles():
    """
    Just returns generate_obstacle function
    """
    return generate_obstacles()


def is_position_blocked(x,y):
    '''
    This function checks if the position you want to go to has a obstacle or if there is no obstacle in the way
    '''
    global obstacles_list
    for i in obstacles_list:
        if i[0] <= x <= i[0]+4 and i[1] <= y <= i[1]+4:
            return True
    return False            


def is_path_blocked(x1,y1,x2,y2):
    
    if y1 > y2 :
        y1,y2 = y2,y1
    
    if x1 > x2 :
        x1,x2 = x2,x1


    if x1 == x2:
        for y in range(y1,y2+1):
            if is_position_blocked(x1,y):
                return True
   
    if y1 == y2:
        for x in range(x1,x2+1):
            if is_position_blocked(x,y1):
                return True
    return False

    
obstacles_list = get_obstacles()
