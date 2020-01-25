# There are also a lot of interesting ways to put user-defined classes to use that don’t involve data from the internet.
# Let’s pull all these mechanics together in a slightly more interesting way than we got with the Point class.
# Remember Tamagotchis, the little electronic pets? As time passed, they would get hungry or bored. You had to clean up
# after them or they would get sick. And you did it all with a few buttons on the device.

# We are going to make a simplified, text-based version of that. In your problem set and in the chapter on Inheritance
# we will extend this further.

# First, let’s start with a class Pet. Each instance of the class will be one electronic pet for the user to take care
# of. Each instance will have a current state, consisting of three instance variables:
#         - hunger, an integer
#         - boredom, an integer
#         - sounds, a list of strings, each a word that the pet has been taught to say

# In the __init__ method, hunger and boredom are initialized to random values between 0 and the threshold for being
# hungry or bored. The sounds instance variable is initialized to be a copy of the class variable with the same name.
# The reason we make a copy of the list is that we will perform destructive operations (appending new sounds to the
# list). If we didn’t make a copy, then those destructive operations would affect the list that the class variable
# points to, and thus teaching a sound to any of the pets would teach it to all instances of the class!

# There is a clock_tick method which just increments the boredom and hunger instance variables, simulating the idea
# that as time passes, the pet gets more bored and hungry.
# The __str__ method produces a string representation of the pet’s current state, notably whether it is bored or hungry
# or whether it is happy. It’s bored if the boredom instance variable is larger than the threshold, which is set as a
# class variable.
# To relieve boredom, the pet owner can either teach the pet a new word, using the teach() method, or interact with the
# pet, using the hi() method. In response to teach(), the pet adds the new word to its list of words. In response to the
# hi() method, it prints out one of the words it knows, randomly picking one from its list of known words. Both hi() and
# teach() cause an invocation of the reduce_boredom() method. It decrements the boredom state by an amount that it reads
# from the class variable boredom_decrement. The boredom state can never go below 0.
# To relieve hunger, we call the feed() method.

from random import randrange


class Pet():
    boredom_decrement = 4
    hunger_decrement = 6
    boredom_threshold = 5
    hunger_threshold = 10
    sounds = ['Mrrp']

    def __init__(self, name="Kitty"):
        self.name = name
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)
        # copy the class attribute, so that when we make changes to it, we won't affect the other Pets in the class
        self.sounds = self.sounds[:]

    def clock_tick(self):
        self.boredom += 1
        self.hunger += 1

    def mood(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            return "happy"
        elif self.hunger > self.hunger_threshold:
            return "hungry"
        else:
            return "bored"

    def __str__(self):
        state = "     I'm " + self.name + ". "
        state += " I feel " + self.mood() + ". "
        # state += "Hunger {} Boredom {} Words {}".format(self.hunger, self.boredom, self.sounds)
        return state

    def hi(self):
        print(self.sounds[randrange(len(self.sounds))])
        self.reduce_boredom()

    def teach(self, word):
        self.sounds.append(word)
        self.reduce_boredom()

    def feed(self):
        self.reduce_hunger()

    def reduce_hunger(self):
        self.hunger = max(0, self.hunger - self.hunger_decrement)

    def reduce_boredom(self):
        self.boredom = max(0, self.boredom - self.boredom_decrement)


# Let’s try making a pet and playing with it a little. Add some of your own commands, too, and keep printing p1 to see
# what the effects are. If you want to directly inspect the state, try printing p1.boredom or p1.hunger.
p1 = Pet("Fido")
print(p1)  # I'm Fido.  I feel happy.
for i in range(10):
    p1.clock_tick()
    print(p1)
#      I'm Fido.  I feel happy.
#      I'm Fido.  I feel happy.
#      I'm Fido.  I feel happy.
#      I'm Fido.  I feel bored.
#      I'm Fido.  I feel bored.
#      I'm Fido.  I feel bored.
#      I'm Fido.  I feel bored.
#      I'm Fido.  I feel hungry.
#      I'm Fido.  I feel hungry.
#      I'm Fido.  I feel hungry.
p1.feed()
p1.hi()
p1.teach("Boo")
for i in range(10):
    p1.hi()
# Mrrp
# Mrrp
# Boo
# Boo
# Boo
# Mrrp
# Mrrp
# Mrrp
# Boo
# Boo
# Boo
print(p1)  # I'm Fido.  I feel happy.
