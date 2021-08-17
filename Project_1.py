
import numpy as np


# Let us define the Initial state
initial_state = np.array([[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12],
              [13,14,15,0]])

print('Initial state:')
print(initial_state)
print(" ")
print(" ")

# Let us also define Goal state
goal_state = np.array([[1,2,3,4],
                       [5,6,7,8],
                       [0,10,11,12],
                       [13,9,14,15]])

# list that keep track of blank tile indices that have been visited
blank = np.array([[0,0,0,0],
                  [0,0,0,0],
                  [0,0,0,0]])
visited_list = [blank]
open_list = [initial_state]

# Finding the blank which is zero in the matrix.
blank_position = np.where(initial_state == 0)
row_blank_position = blank_position[0][0]
col_blank_position = blank_position[1][0]

# adding the state zero in the visited list
# visited_list.append(initial_state)
    
a = initial_state


################################################################################################
# function for moving our blank up
def up(a):
    
    # finding indices for blank position
    blank_position = np.where(a == 0)
    row_blank_position = blank_position[0][0]
    col_blank_position = blank_position[1][0]
    
    # if is used here to check for the condition when blank can not move up as it is already in the top most row
    # also for the condition if the new place has been visited before or not
    if (row_blank_position != 0):
        
        # movement of blank in the up direction and interchanging the value that was above blank
        place_holder = a[row_blank_position - 1][col_blank_position]  # holds the value above blank temporarily
        a[row_blank_position][col_blank_position] = place_holder
        a[row_blank_position - 1][col_blank_position] = 0

        # return values to know if movement was successful
        return True
    else:
        return False
          

# function for moving our blank down
def down(a):

    # finding indices for blank position
    blank_position = np.where(a == 0)
    row_blank_position = blank_position[0][0]
    col_blank_position = blank_position[1][0]
    
    if (row_blank_position != 3):
        
        place_holder = a[row_blank_position + 1][col_blank_position] 
        a[row_blank_position][col_blank_position] = place_holder
        a[row_blank_position + 1][col_blank_position] = 0
             
                # return values to know if movement was successful
        return True
    else:
        return False
          
 
# function for moving our blank left
def left(a):
    
    # finding indices for blank position
    blank_position = np.where(a == 0)
    row_blank_position = blank_position[0][0]
    col_blank_position = blank_position[1][0]
    
    if (col_blank_position != 0):
        
        place_holder = a[row_blank_position][col_blank_position - 1]  # holds the value above blank temporarily
        a[row_blank_position][col_blank_position] = place_holder
        a[row_blank_position][col_blank_position - 1] = 0
  
        # return values to know if movement was successful
        return True
    else:
        return False
        

# function for moving our blank right
def right(a):

    # finding indices for blank position
    blank_position = np.where(a == 0)
    row_blank_position = blank_position[0][0]
    col_blank_position = blank_position[1][0]
    
    if (col_blank_position != 3):
        
        place_holder = a[row_blank_position][col_blank_position + 1]  # holds the value above blank temporarily
        a[row_blank_position][col_blank_position] = place_holder
        a[row_blank_position][col_blank_position + 1] = 0

                # return values to know if movement was successful
        return True
    else:
        return False

################################################################################################################3

while True:
    
    a = open_list[0]

    if up(a):
        u = a.copy()
        open_list.append(u)
        if np.array_equal(a,goal_state) == True:
            break
        down(a)
        
    if down(a):
        d = a.copy()
        open_list.append(d)
        if np.array_equal(a,goal_state) == True:
            break
        up(a)
        
    if left(a):
        l = a.copy()
        open_list.append(l)
        if np.array_equal(a,goal_state) == True:
            break
        right(a)
        
    if right(a):
        r = a.copy()
        open_list.append(r)
        if np.array_equal(a,goal_state) == True:
            break
        left(a)
    
    ree = open_list.pop(0)
    
    # delete all the states in open the same as we checked
    uniques = []
    for arr in open_list:
        if not any(np.array_equal(arr, unique_arr) for unique_arr in uniques):
            uniques.append(arr)
    
    open_list = uniques

    print(a)
    print('-----------')

print('goal reached')
