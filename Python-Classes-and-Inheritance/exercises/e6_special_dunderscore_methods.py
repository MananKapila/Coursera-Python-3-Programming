# Dunderscore = double underscore

# Suppose we have our point class from before, where we defined the __init__ constructor and the __str__ conversion
# method.


class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def __str__(self):
        return "x = {}, y = {}".format(self.x, self.y)


# Now suppose we have to instances of this point class.
p1 = Point(-5, 10)
p2 = Point(0, 3)


# Suppose that we wanted the ability to be able to add points together. So, for example, if we take p1 plus p2, then we
# might want to create a new point by adding their x and y coordinates.
# But if we write print(p1 + p2) we're going to get an error saying that we can't add points.
# In other words, when we tell Python that we want to add these two point instances, Python doesn't know how to actually
# take these instances and produce something that represents their values added together.

# But we can override a method called __add__ that will tell Python how to actually add two points together!


class Point:

    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def __str__(self):
        return "x = {}, y = {}".format(self.x, self.y)

    # __add__ is going to take in self, but it's also going to take in what we're expecting to add to self.
    def __add__(self, otherPoint):
        return Point(self.x + otherPoint.x, self.y + otherPoint.y)


p1 = Point(-5, 10)
p2 = Point(0, 3)
# Now, as soon as we define this __add__ method, when we print out the value of p1 plus p2, we're going to see that we
# get a new point at -5 and 13.
print(p1 + p2)  # x = -5, y = 13


# Beyond add, there are several other methods that we can override. For example, there is subtraction.
class Point:

    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def __str__(self):
        return "x = {}, y = {}".format(self.x, self.y)

    def __add__(self, otherPoint):
        return Point(self.x + otherPoint.x, self.y + otherPoint.y)

    def __sub__(self, otherPoint):
        return Point(self.x - otherPoint.x, self.y - otherPoint.y)


p1 = Point(-5, 10)
p2 = Point(0, 3)
print(p1 - p2)  # x = -5, y = 7

# There are many other methods that we can override, but they follow the same pattern as add, sub, and they all start
# and end with dunderscores.
