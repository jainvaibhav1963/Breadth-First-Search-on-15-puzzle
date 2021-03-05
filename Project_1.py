# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 20:20:36 2021

@author: jain
"""

import numpy as np





# Let us define the Initial state
a = np.array([[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12],
              [13,14,15,0]])

print('Initil state:')
print(a)
print(" ")

# Let us also define Goal state
goal_state = np.array([[1,2,3,4],
                       [5,6,7,8],
                       [9,10,11,12],
                       [13,14,0,15]])

# list that keep track of blank tile indices that have been visited
visited_list = []

# a list to store states
a_list = []

# Finding the blank which is zero in the matrix.
blank_position = np.where(a == 0)
row_blank_position = blank_position[0][0]
col_blank_position = blank_position[1][0]

# adding the position of zero in the visited list
visited_list.append([row_blank_position, col_blank_position])
    



################################################################################################
# function for moving our blank up
def up():
    
    global blank_position
    global row_blank_position
    global col_blank_position
    
    # finding indices for blank position
    blank_position = np.where(a == 0)
    row_blank_position = blank_position[0][0]
    col_blank_position = blank_position[1][0]
    
    
    # if is used here to check for the condition when blank can not move up as it is already in the top most row
    # also for the condition if the new place has been visited before or not
    if (row_blank_position != 0) and ([row_blank_position - 1,col_blank_position] not in visited_list):
        
        # movement of blank in the up direction and interchanging the value that was above blank
        place_holder = a[row_blank_position - 1][col_blank_position]  # holds the value above blank temporarily
        a[row_blank_position][col_blank_position] = place_holder
        a[row_blank_position - 1][col_blank_position] = 0
        
        # add that position in the visited list
        visited_list.append([row_blank_position - 1,col_blank_position])

        # return values to know if movement was successful
        return True
    else:
        return False
          

# function for moving our blank down
def down():
    
    global blank_position
    global row_blank_position
    global col_blank_position
    
    # finding indices for blank position
    blank_position = np.where(a == 0)
    row_blank_position = blank_position[0][0]
    col_blank_position = blank_position[1][0]
    
    
    if (row_blank_position != 3) and ([row_blank_position + 1,col_blank_position] not in visited_list):
        
        place_holder = a[row_blank_position + 1][col_blank_position] 
        a[row_blank_position][col_blank_position] = place_holder
        a[row_blank_position + 1][col_blank_position] = 0
        
        visited_list.append([row_blank_position + 1,col_blank_position]) 

             
                # return values to know if movement was successful
        return True
    else:
        return False
          
 
# function for moving our blank left
def left():
    
    global blank_position
    global row_blank_position
    global col_blank_position
    
    # finding indices for blank position
    blank_position = np.where(a == 0)
    row_blank_position = blank_position[0][0]
    col_blank_position = blank_position[1][0]
    
    
    if (col_blank_position != 0) and ([row_blank_position,col_blank_position - 1] not in visited_list):
        
        place_holder = a[row_blank_position][col_blank_position - 1]  # holds the value above blank temporarily
        a[row_blank_position][col_blank_position] = place_holder
        a[row_blank_position][col_blank_position - 1] = 0
  
        visited_list.append([row_blank_position,col_blank_position - 1]) 
        
  
        # return values to know if movement was successful
        return True
    else:
        return False
          
                

# function for moving our blank right
def right():
    
    global blank_position
    global row_blank_position
    global col_blank_position
    
    # finding indices for blank position
    blank_position = np.where(a == 0)
    row_blank_position = blank_position[0][0]
    col_blank_position = blank_position[1][0]
    
    
    if (col_blank_position != 3) and ([row_blank_position,col_blank_position + 1] not in visited_list):
        
        place_holder = a[row_blank_position][col_blank_position + 1]  # holds the value above blank temporarily
        a[row_blank_position][col_blank_position] = place_holder
        a[row_blank_position][col_blank_position + 1] = 0
        
        # add that position in the visited list
        visited_list.append([row_blank_position,col_blank_position + 1])

                # return values to know if movement was successful
        return True
    else:
        return False

################################################################################################################3

  
#################################################################################################################

# obtaining the very first children of the initial state

if up() == True:
    visited_list.remove([row_blank_position,col_blank_position]) #>>> take down place out of visited list
    
    # child in first layer
    child_up_1 = a.copy()
    print(child_up_1)
    
    down() #go back to original poition

      
if down() == True:
    visited_list.remove([row_blank_position,col_blank_position]) #>>> take up out of visited list
    
    child_down_1 = a.copy()
    print(child_down_1)
    
    up()
    
        
if left() == True:
    visited_list.remove([row_blank_position,col_blank_position]) #>>> take right out of visited list
    child_left_1 = a.copy()
    print(child_left_1)
    
    right()

            
if right() == True:
    
    visited_list.remove([row_blank_position,col_blank_position]) #>>> take left position out of visited list
    child_right_1 = a.copy()
    print(child_right_1)
    
    left()
    
print("visited_list:")    
print(visited_list)   #>>> ouputs the visited list
print(" ")
  
 #################################################################################################################################
   
# main
# now we try to create a nested loop to implement BFS


static_list = [visited_list] #>>>>> List that holds the visited list without changing for the inner loop

print(static_list)

# j = 0
# while np.array_equal(goal_state,a) == False:

# for loop takes a maximum value of how many steps in BFS we want
for j in range(10):   #>>> this can be a while loop to give conition for goal state reaching
    
    
    size = len(static_list[j]) - 1  #>>>> inner loop doesn't iterate over the first value and the last value
                                    #>>>> why? because, first value is where blank tile came from and last value signifies where blank tile is at right now. The values in between are children
    
   
    for i in range(size):
        
        if (j == 0):
            
        # this is where my new zero/blank-tile should be
            [new_row_blank, new_col_blank] = static_list[j][i]
        else:
            [new_row_blank, new_col_blank] = static_list[j][i+1]
        
        
        # this is where my old zero is
        blank_position = np.where(a == 0)
        row_blank_position = blank_position[0][0]
        col_blank_position = blank_position[1][0]
          
        
        # Interchanging values between new zero and old zero positions
        x = a[new_row_blank][new_col_blank]
        a[row_blank_position][col_blank_position] = x
        a[new_row_blank][new_col_blank] = 0   #>>>>> new blank_tile
        
        
        # just saving the parents in the visited list, the first value which signifies where the blank tile came from
        visited_list = [static_list[j][-1]]
        
        #add the new zero position to the visited list
        visited_list.append([new_row_blank, new_col_blank])
        
        
        if up() == True:
            
            visited_list.remove([row_blank_position,col_blank_position]) #>>> take down position out of visited list
            
            # child in first layer
            child_up_1 = a.copy()
            print(child_up_1)
            
            down() #go back to original poition
            # down() #attempt to go to a different position
              
            
        if down() == True:
            visited_list.remove([row_blank_position,col_blank_position]) #>>> take up out of visited list

            child_down_1 = a.copy()
            print(child_down_1)
            
            up()
            
            
        if left() == True:
            visited_list.remove([row_blank_position,col_blank_position]) #>>> take right out of visited list
            child_left_1 = a.copy()
            print(child_left_1)
            
            right()
    
            
        if right() == True:
        
            visited_list.remove([row_blank_position,col_blank_position]) #>>> take left position out of visited list
            child_right_1 = a.copy()
            print(child_right_1)
            
            left()
            
            
        print(visited_list)
        print('')
        
        
        # if (a in a_list):
        #     continue
        
        
        static_list.append(visited_list) #>>>> update the static list with the new visited list 
    

    j += 1  
    
    
        
        
    
    



    
    




    