# We previously learned how to sort lists (e19_sorting_key_parameter).
L = ["Cherry", "Apple", "Blueberry"]
print(sorted(L, key=len))
# alternative form using lambda, if you find that easier to understand
print(sorted(L, key=lambda x: len(x)))


# Sorting lists of instances of a class is not fundamentally different from sorting lists of objects of any other type.
# There is a way to define a default sort order for instances, right in the class definition, but it requires defining
# a bunch of methods or one complicated method, so we won’t bother with that. Instead, we should just provide a key
# function as a parameter to sorted (or sort).
# When each of the items in a list is an instance of a class, we need to provide a function that takes one instance as
# an input, and returns a number. The instances will be sorted by their numbers.
class Fruit:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return "[{} , {}]".format(self.name, self.price)


L = [Fruit("Cherry", 10), Fruit("Apple", 5), Fruit("Blueberry", 20)]
print(sorted(L, key=lambda x: x.price))  # [<__main__.Fruit object at 0x7fed089f4908>,
# <__main__.Fruit object at 0x7fed089f48d0>, <__main__.Fruit object at 0x7fed089f4940>]
# We remember that printing an entire list of instances won't use the custom __str__ functions defined in their classes.
# So in order to have a pretty print, we have to manually print every instance individually.
for f in sorted(L, key=lambda x: x.price):
    print(f)


# [Apple , 5] [Cherry , 10] [Blueberry , 20]

# Sometimes we will find it convenient to define the sorting method inside the class, in order to better isolate the
# sorting logic applied to any particular instance of that class. Naturally, the method still has to return a number.
class Fruit:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return "[{} , {}]".format(self.name, self.price)

    def sort_priority(self):
        return self.price


# In order to specify an instance method as the key parameter to the sort function, we use the syntax:

L = [Fruit("Cherry", 10), Fruit("Apple", 5), Fruit("Blueberry", 20)]
print("-----sorted by price, referencing a class method-----")
for f in sorted(L, key=Fruit.sort_priority):
    print(f)

print("---- one more way to do the same thing-----")
for f in sorted(L, key=lambda x: x.sort_priority()):
    print(f)
