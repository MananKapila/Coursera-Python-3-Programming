# The split method splits a string into a list of sub-strings, based on
# an optional delimiter. If none is specified, the default delimiter si
# the space string ' '.
song = "The rain in Spain..."
wds = song.split()
print(wds)              # ['The', 'rain', 'in', 'Spain...']
song = "The rain in Spain..."
wds = song.split('ai')
print(wds)              # ['The r', 'n in Sp', 'n...']

# The join method does the reverse, which is joining a list of strings
# into one by concatenating them with the delimiter it's called on.
wds = ["red", "blue", "green"]
glue = ';'
s = glue.join(wds)
print(s)                # red;blue;green
print(wds)              # ['red', 'blue', 'green']
print("***".join(wds))  # red***blue***green
print("".join(wds))     # redbluegreen





