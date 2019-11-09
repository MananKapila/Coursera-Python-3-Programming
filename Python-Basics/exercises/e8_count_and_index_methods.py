# Sequences have two useful methods: count and index
# The count method returns the number of times a certain element appears
# in the sequence.
a = "I have had an apple on my desk before!"
print(a.count("e"))     # 5
print(a.count("ha"))    # 2

z = ['atoms', 4, 'neutron', 6, 'proton', 4, 'electron', 4, 'electron', 'atoms']
print(z.count("4"))             # 0
print(z.count(4))               # 3
print(z.count("a"))             # 0
print(z.count("electron"))      # 2

# The index method returns the index where the first appearance of an element
# occurs in a sequence.
music = "Pull out your music and dancing can begin"
print(music.index("m"))         # 14
print(music.index("your"))      # 9

bio = ["Metatarsal", "Metatarsal", "Fibula", [], "Tibia", "Tibia", 43, "Femur", "Occipital", "Metatarsal"]
print(bio.index("Metatarsal"))  # 0
print(bio.index([]))            # 3
print(bio.index(43))            # 6

# If the specified element doesn't appear at all in the sequence, a run-time
# error will occur.
seasons = ["winter", "spring", "summer", "fall"]
# print(seasons.index("autumn"))  # Error!

# It's important to note that both index and count are case-sensitive!
qu = "wow, welcome week! Were you wanting to go?"
ty = qu.count("we")     # 2, because there's a difference between 'we' and 'We'





