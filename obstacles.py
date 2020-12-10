"""
[Module] obstacle module is in world package
"""


import random

#list which will be filled with obstacle co-ordinates
obstacles_list = []


def generate_obstacles():
    """
    get obstacles:
        creates a list ob_list which creates a random x and y list,
        using the parameters given
        returns them as a list of tuples with x and y co-ordinates
    """
    global obstacles_list
 
    obstacles_list = [(random.randint(-95,95),random.randint(-190,190)) for i in range(0,random.randint(1,10))]
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
    
    elif x1 > x2 :
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


