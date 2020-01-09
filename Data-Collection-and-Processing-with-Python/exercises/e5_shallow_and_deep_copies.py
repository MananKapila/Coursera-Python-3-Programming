# Earlier when we discussed cloning and aliasing lists we had mentioned that simply cloning a list using [:] would take
# care of any issues with having two lists unintentionally connected to each other. (see e20_cloning_lists). That was
# definitely true for making shallow copies (copying a list at the highest level), but as we get into nested data and
# nested lists in particular, the rules become a bit more complicated. We can have second-level aliasing in these cases,
# which means we need to make deep copies.

# When you clone a nested list using [:], you don't also get clones of the internal lists. What you will get is aliases
# of them. This means that if you perform a mutation operation on one of the original sublists, the aliased version will
# also change. We can see this happen in the following nested list, which only has two levels.
original = [['dogs', 'puppies'], ['cats', "kittens"]]
copied_version = original[:]
print(copied_version)  # [['dogs', 'puppies'], ['cats', 'kittens']]
print(copied_version is original)  # False
print(copied_version == original)  # True
original[0].append(["canines"])
print(original)  # [['dogs', 'puppies', ['canines']], ['cats', 'kittens']]
print("-------- Now look at the copied version -----------")
print(copied_version)  # [['dogs', 'puppies', ['canines']], ['cats', 'kittens']]
# We see that it's the same!
print("\n")

# If we don’t want to have aliased lists inside of our nested list, then we’ll need to obtain a deep copy of the
# "original" nested list.

# One way of achieving this is by using nested iteration:
original = [['dogs', 'puppies'], ['cats', "kittens"]]
copied_outer_list = []
for inner_list in original:
    copied_inner_list = []
    for item in inner_list:
        copied_inner_list.append(item)
    copied_outer_list.append(copied_inner_list)
print(copied_outer_list)  # [['dogs', 'puppies'], ['cats', 'kittens']]
original[0].append(["canines"])
print(original)  # [['dogs', 'puppies', ['canines']], ['cats', 'kittens']]
print("-------- Now look at the copied version -----------")
print(copied_outer_list)  # [['dogs', 'puppies'], ['cats', 'kittens']]
# Not the same anymore!
print("\n")

# Or, equivalently, we could take advantage of the slice operator to do the copying of the inner list.
original = [['dogs', 'puppies'], ['cats', "kittens"]]
copied_outer_list = []
for inner_list in original:
    copied_inner_list = inner_list[:]
    copied_outer_list.append(copied_inner_list)
print(copied_outer_list)
original[0].append(["canines"])
print(original)
print("-------- Now look at the copied version -----------")
print(copied_outer_list)
# Obviously, we obtain the same results as earlier.
print("\n")

# This process of neste iteration we used above works fine when there are only two layers or levels in a nested list.
# However, if we want to make a copy of a nested list that has more than two levels, then we recommend using the copy
# module. In the copy module there is a method called deepcopy that will take care of the operation for you.

import copy

original = [['canines', ['dogs', 'puppies']], ['felines', ['cats', 'kittens']]]
shallow_copy_version = original[:]
deeply_copied_version = copy.deepcopy(original)
original.append("Hi there")
original[0].append(["marsupials"])
print("-------- Original -----------")
print(original)  # [['canines', ['dogs', 'puppies'], ['marsupials']], ['felines', ['cats', 'kittens']], 'Hi there']
print("-------- deep copy -----------")
print(deeply_copied_version)  # [['canines', ['dogs', 'puppies']], ['felines', ['cats', 'kittens']]]
print("-------- shallow copy -----------")
print(shallow_copy_version)  # [['canines', ['dogs', 'puppies'], ['marsupials']], ['felines', ['cats', 'kittens']]]
