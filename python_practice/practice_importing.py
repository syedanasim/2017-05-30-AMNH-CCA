'''
Here is the docstring:
We will use this to see how we can import from another module
'''

import practice_script as ps

print (ps.sample_int)
myalg = ps.Algebra(1.5, 5.0)
#No print statement below
myalg.multiply() #This *does* have return value
print (myalg.multiply())

for x in [1,3,5]:
#Let's loop different values for the first argument in the Algebra class
    myalg = ps.Algebra(x, 5.0)
    print (myalg.add())
    print (myalg.x)
    print (myalg.y)
