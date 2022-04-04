# Countdown - Create a function that accepts a number as an input. 
# Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
def countdown(number): #number is 15
    new_list = [] #empty list
    for i in reversed(range(number+1)): #reversed is a keyword in python
        new_list.append(i) #i is(5,4,3,2,1,0)
    return new_list
print(countdown(5)) #output:[5, 4, 3, 2, 1, 0]


# Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
def print_and_return(list): #list is [1,2]
    print(list[0]) #will print 1
    return(list[1]) #return value is 2
print(print_and_return([1,2])) #output:1,2


# First Plus Length - Create a function that accepts a list 
# And returns the sum of the first value in the list plus the list's length.
def print_and_return(list):
    return len(list)+list[0] #returns the length of the list plus the first value
print(print_and_return([1,2,3,4,5])) #output:6
print(print_and_return([6,2,3,4,5])) #output:11


# Values Greater than Second - Write a function that accepts a list 
# and creates a new list containing only the values from the original list that are greater than its 2nd value. 
# Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
def values_greater_than_second(list):                #  got help from solutions
    if len(list) < 2: # this is the list:[5,2,3,2,1,4]
        return False
    new_list = [] #empty list
    for i in list:
        if i > list[1]:  # i is 5,2,3,2,1,4
            new_list.append(i) #values that are lesser than the 2nd value(2) will get pushed to the new list
    print(len(new_list))    #length of new list will be printed
    return new_list # then new list will be printed
print(values_greater_than_second([5,2,3,2,1,4])) # output:3 [5,3,4]
print(values_greater_than_second([5])) #output:False
print(values_greater_than_second([3,4])) # output:[]


# This Length, That Value - Write a function that accepts two integers as parameters: size and value. 
# The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
def this_length_that_value(size, value):  #takes in two parameters(size and value)
    list = []        #creates a new list
    for i in range(size): #size:4 and value:7     (i=0,1,2,3)
            list.append(value) #push the value to the list 
    return list 
print(this_length_that_value(4,7)) # output: [7,7,7,7]
print(this_length_that_value(6,2)) #output: [2,2,2,2,2,2]
