# algorithm for max_int


# get number as input
num_int = int(input("Input a number: "))    # Do not change this line
max_int = 0

# is it negative?
while num_int >= 0:
    num_int = int(input("Input a number: "))
    if num_int >= max_int:
        max_int = num_int

# if not ask for another number

# if it is negative, print the 
# highest number the user has inputed
print("The maximum is", max_int)    # Do not change this line
