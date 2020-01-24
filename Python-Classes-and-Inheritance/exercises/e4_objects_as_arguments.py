# You can pass an object as an argument to a function, in the usual way.
# Here is a simple function called distance involving our new Point objects. The job of this function is to figure out
# the distance between two points.
import math


class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5


def distance(point1, point2):
    xdiff = point2.getX() - point1.getX()
    ydiff = point2.getY() - point1.getY()

    dist = math.sqrt(xdiff ** 2 + ydiff ** 2)
    return dist


p = Point(4, 3)
q = Point(0, 0)
print(distance(p, q))  # 5


# The distance function takes two points and returns the distance between them. Note that distance is not a method of
# the Point class. You can see this by looking at the indentation pattern. It is not inside the class definition.
# The other way we can know that distance is not a method of Point is that self is not included as a formal parameter.
# In addition, we do not invoke distance using the dot notation.

# We could have made distance be a method of the Point class. Then, we would have called the first parameter self, and
# would have invoked it using the dot notation, as in the following code. Which way to implement it is a matter of
# coding style. Both work correctly. Most programmers choose whether to make functions be stand-alone or methods of a
# class based on whether the function semantically seems to be an operation that is performed on instances of the class.
# In this case, because distance is really a property of a pair of points and is symmetric (the distance from a to b is
# the same as that from b to a) it makes more sense to have it be a standalone function and not a method. Many heated
# discussions have occurred between programmers about such style decisions.


class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def distance(self, point2):
        xdiff = point2.getX() - self.getX()
        ydiff = point2.getY() - self.getY()

        dist = math.sqrt(xdiff ** 2 + ydiff ** 2)
        return dist


p = Point(4, 3)
q = Point(0, 0)
print(p.distance(q))  # 5

# Observation: we would've gotten the same results if instead of having getters we accessed the x and y properties
# directly (self.x, self.y, point1.x, point1.y, point1.x ,point1.y)
