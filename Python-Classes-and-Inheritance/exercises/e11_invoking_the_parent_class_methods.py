# In the previous exercise, we've seen how we can override methods and class variables.
# But how do we invoke a parent class's method inside the child class?
# There are two options for doing this:

class Person():
    def __init__(self, age):
        self.age = age

    def get_old(self):
        self.age += 1
        print("I got older, I'm {} now.".format(self.age))


# Option 1: (we've used it in the previous exercise inside the Dog class's __init__ method)

class Optimist(Person):
    def get_old(self):
        # HERE
        Person.get_old(self)
        print("That means I'm wiser! :)")


p = Person(54)
p.get_old()  # I got older, I'm 55 now.

o = Optimist(54)
o.get_old()  # I got older, I'm 55 now. That means I'm wiser! :)


# Option 2: pessimist

class Pessimist(Person):
    def get_old(self):
        # HERE - notice that we don't have to specify the parent class' name or pass the self instance-variable anymore
        super().get_old()
        print("Closer to the end...")


pp = Pessimist(63)
pp.get_old()  # I got older, I'm 64 now. Closer to the end...

# The second approach is nicer because it's easier to read and it eliminates the need of specifying the name of the
# parent class anywhere else after the child's header.
