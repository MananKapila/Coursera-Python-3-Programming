# We have already seen that each instance of a class has its own namespace with its own instance variables.
# Two instances of the Point class each have their own instance variable x. Setting x in one instance doesn’t affect
# the other instance.

# A class can also have class variables. A class variable is set as part of the class definition.

# For example, consider the following version of the Point class. Here we have added a graph method that generates a
# string representing a little text-based graph with the Point plotted on the graph. It’s not a very pretty graph,
# in part because the y-axis is stretched like a rubber band, but we can get the idea from this.

# Note that there is an assignment to the variable printed_rep on line 19. It is not inside any method. That makes it
# a class variable. It is accessed in the same way as instance variables. For example, on line 31, there is a reference
# to self.printed_rep. If we change line 19, we have it print a different character at the x,y coordinates of the Point
# in the graph.

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    printed_rep = "*"

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def graph(self):
        rows = []
        size = max(int(self.x), int(self.y)) + 2
        for j in range(size - 1):
            if (j + 1) == int(self.y):
                special_row = str((j + 1) % 10) + (" " * (int(self.x) - 1)) + self.printed_rep
                rows.append(special_row)
            else:
                rows.append(str((j + 1) % 10))
        rows.reverse()  # put higher values of y first
        x_axis = ""
        for i in range(size):
            x_axis += str(i % 10)
        rows.append(x_axis)

        return "\n".join(rows)


p1 = Point(2, 3)
p2 = Point(3, 12)
print(p1.graph())
# 4
# 3 *
# 2
# 1
# 01234
print()
print(p2.graph())
# 3
# 2  *
# 1
# 0
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# 01234567890123

# To be able to reason about class variables and instance variables, it is helpful to know the rules that the python
# interpreter uses. That way, we can mentally simulate what the interpreter does.

# When the interpreter sees an expression of the form <obj>.<varname>, it:
#       1. Checks if the object has an instance variable with that name set. If so, it uses that value.
#       2. If it doesn't find an instance variable, it checks whether the class has a class variable with that name.
#           If so, it uses that value.
#       3. If it doesn't find an instance or a class variable, it creates a runtime error (actually, it does one other
#           check first, which we will learn about in the next chapter).

# When the interpreter sees an assignment statement of the form <obj>.<varname> = <expr>, it:
#       1. Evaluates the expression on the right-hand side to yield some python object;
#       2. Sets the instance variable <varname> of <obj> to be bound to that python object. Note that an assignment
#           statement of this form NEVER sets the class variable; it only sets the instance variable.

# In order to set a class variable, we can either do that:
#       - inside the class, by using an assignment statement of the form <varname> = <expr> at the top-level (line 19)
#       - outside the class, by using an assignment statement of the form <classname>.<varname> = <expr> (line 87)
Point.printed_rep = "A"
print(p1.graph())
# 4
# 3 A
# 2
# 1
# 01234

# Method definitions also create homonymous class variables. Thus, in the code above, graph becomes a class variable
# that is bound to a function/method object.
# p1.graph() is evaluated by:
#       - looking up p1 and finding that it’s an instance of Point
#       - looking for an instance variable called graph in p1, but not finding one
#       - looking for a class variable called graph in p1’s class, the Point class; it finds a function/method object
#       - Because of the () after the word graph, it invokes the function/method object, with the parameter self bound
#           to the object p1 points to.
