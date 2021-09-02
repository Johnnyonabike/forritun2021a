

# calculating a summing the sequence formula
# finally printing out the sum
# user will be asked for a number n
n = int(input("Enter the length of the sequence: ")) # Do not change this line

a = 0
b = 1
c = 2

# a for loop run for n times
# calculating the sequence formula
# finally printing out the sums

if n >= b:
    print(b)
if n >= c:
    print(c)
if n > c:
    for i in range(0,n-2):
        d = a+b+c
        a = b
        b = c
        c = d
        print(d)
