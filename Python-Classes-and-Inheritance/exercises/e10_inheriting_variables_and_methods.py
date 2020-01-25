# In order to explore inheritance, we will use the classic Animal example.


class Animal:
    sounds = ["..."]

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # cloning the class attribute, so that when we make changes to it, we won't affect the other Animal instances
        self.sounds = self.sounds[:]

    def __str__(self):
        return "{} ({} years old)".format(self.name, self.age)

    def make_sounds(self):
        sounds_string = ""
        for sound in self.sounds:
            sounds_string += sound + " "
        print("{} : {}".format(self.name, sounds_string))


a = Animal("kiki", 3)
print(a)  # kiki (3 years old)
a.make_sounds()  # kiki : ...


# Now let's extends the Animal class by a class called Dog.
# But before we move on, we have to make two important statements about constructors (init methods) in Python.

# ========================================================================= #
# In Python you can only define ONE constructor (init method)!
# ========================================================================= #

# ========================================================================= #
# In Python, all classes inherit all methods of their superclass, including
# __init__. That means CLASSES INHERIT CONSTRUCTORS.
# ========================================================================= #

# We notice that Python differs from Java in the two aspects mentioned above.
# They also help explain the errors arising from the following scenarios:

class Dog(Animal):
    pass
    # Let's not specify any constructor first.


d = Dog(5, "Sally")  # This works well because Dog inherited Animal's constructor.


# d = Dog()
# TypeError: __init__() missing 2 required positional arguments: 'name' and 'age'
# It didn't work because Dog inherits the Animal constructor with two actual parameters: name and age. So THAT is the
# constructor Dog HAS to use.

class Dog(Animal):
    def __init__(self):
        print("i'm a do-nothing constructor")

    def __init__(self, age):
        self.age = age


# d = Dog()
# TypeError: __init__() missing 1 required positional argument: 'age'
# Calling the no-actual-parameters constructor didn't work because it preceded the one-actual-parameter constructor in
# the class definition. Python won't actually give us an error if we define multiple __init__ methods inside a class,
# it will just use the one we defined last and ignore the previous ones!

# So this will be the one that will work:
d = Dog(5)
print(d.age)  # 5


# print(d.name)
# AttributeError: 'Dog' object has no attribute 'name'

# d = Dog("Sally", 5)
# TypeError: __init__() takes 2 positional arguments but 3 were given
# This doesn't work either. We can't call Animal's constructor on Dog anymire because there can only be one valid
# constructor in any class and Dog defined its own. Therefore, the last-defined __init__ method of the child class
# replaced the parent's constructor.


class Dog(Animal):
    # We will stick with the two-actual-parameters constructor, but we will provide some additional functionality
    # compared to the one in Animal.
    def __init__(self, age, name):
        # It would be a waste of code not to actually call the parent's constructor if we want to do the same things.
        Animal.__init__(self, age, name)
        # And now the new bit: we want dogs to have collar inscriptions.
        self.collar_inscription = "Return to owner."


d = Dog("Sally", 5)
print(d.age)  # 5
print(d.name)  # Sally
print(d.collar_inscription)  # Return to owner.

d.make_sounds()  # Sally : ...
# We notice that Dog inherited the make_sounds instance method.
print(d)  # Sally (5 years old)
# Dog also inherited the __str__ class method.

print(d.sounds)  # ['...']
print(Dog.sounds)  # ['...']


# We notice that Dog inherited the class variable from Animal.

class Dog(Animal):
    # Let's override the sounds class variable.
    sounds = ["...", "bark"]

    def __init__(self, age, name):
        Animal.__init__(self, age, name)
        self.collar_inscription = "Return to owner."


d = Dog("Sally", 5)
print(Dog.sounds)  # ['...', 'bark']
# We have successfully overwritten sounds.

print(d.sounds)  # ['...', 'bark']
d.sounds.append("howl")
print(d.sounds)  # ['...', 'bark', 'howl']
print(Dog.sounds)  # ['...', 'bark']
# We notice that Dog.sounds (the class variable) remained unaffected by the change in d.sounds (which is an instance
# variable).
# This is because we took care not to propagate this kind of changes when we cloned the class variable in Animal's
# constructor.

d.make_sounds()  # Sally : ... bark
print(d)  # Sally (5 years old)


# So what is happening in the Python interpreter when we write programs with classes, subclasses, and instances of
# both parent classes and subclasses?

# This is how the interpreter looks up attributes (variables and methods):
#     1. First, it checks for an instance variable or an instance method by the name it’s looking for.
#     2. If an instance variable or method by that name is not found, it checks for a class variable.
#     3. If no class variable is found, it looks for a class variable in the parent class.
#     4. If no class variable is found, the interpreter looks for a class variable in THAT class’s parent
#       (the “grandparent” class).
#     5. This process goes on until the last ancestor is reached, at which point Python will signal an error.

