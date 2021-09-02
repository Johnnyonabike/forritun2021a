

# calculating a summing the sequence formula
# finally printing out the sum
# user will be asked for a number n
n = int(input("Enter the length of the sequence: ")) # Do not change this line

a = 0
b = 1
c = 2

# a for loop run for n times
# calculating a summing the sequence formula
# finally printing out the sum
print(b)
for i in range(1,n+1):
    d = a+b+c
    a = b
    b = c
    c = d
    print(d)
