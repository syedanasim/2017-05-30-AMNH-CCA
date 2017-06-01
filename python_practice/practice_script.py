'''
This script contains an example class that we will write. The class will be be called algebra, and it will contain some simple methods to do some algebraic manipulation.

>The script will end with a sample way to call and use the class.
'''
sample_int=5
print (sample_int)

class Algebra:
    def __init__( self, x, y):
        #We are defining the arguments as attributes of the object itself
        self.x = x
        self.y = y
    def add( self ):
        return self.x + self.y
    def subtract( self ):
        return self.x - self.y
    def multiply( self ):
        return self.x * self.y
    def divide( self ):
        return self.x / self.y

    def complicated_algebra( self ):
        return self.multiply() / self.subtract()
    def modify_x( self ):
        self.x = self.x * 2

if __name__ == "__main__" :
    # Create instance of Algebra
    myalg = Algebra(100, 150)
    # Print some outsputs using the Algebra class
    print (myalg.multiply())
    myalg.modify_x()
    print (myalg.multiply())

else:
    print ("name not equal to main")
    print (__name__)
