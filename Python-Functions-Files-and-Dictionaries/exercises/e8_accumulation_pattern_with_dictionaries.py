# We'll now work with a larger text file.
f = open("../my_data/scarlet.txt", 'r')

# Let's say we want to count the number of times the letter 't' occurs
text = f.read()
t_count = 0
for c in text:
    if c == 't':
        t_count += 1
print(t_count)  # 211

# Maybe we also want to count the number of times 's' occurs
t_count = 0
s_count = 0
for c in text:
    if c == 't':
        t_count += 1
    elif c == 's':
        s_count += 1
print(t_count)  # 211
print(s_count)  # 139

# We notice already that the more letters we want to count, the more accumulated variables we have to create.
# If we want, for example, to count every letter in the alphabet, using 27 accumulated variables and elif-statements
# would be too lengthy, code-wise.

# One alternative is using a dictionary for our accumulated variables.
letter_counts = {}
letter_counts['t'] = 0
letter_counts['s'] = 0
for c in text:
    if c == 't':
        letter_counts['t'] += 1
    elif c == 's':
        letter_counts['s'] += 1
print(letter_counts['t'])  # 211
print(letter_counts['s'])  # 139
# So far, though, our code has not gotten more concise.

# But we can easily optimize it. We notice that the if statements are somewhat unnecessary when we want to count every
# character.
letter_counts = {}
for c in text:
    if c not in letter_counts:
        # we have not seen this character before, so we initialize a counter for it
        letter_counts[c] = 0
    letter_counts[c] += 1
print(letter_counts['t'])  # 211
print(letter_counts['s'])  # 139
print(letter_counts['a'])  # 174
print(letter_counts['b'])  # 31

# This is, essentially, the dictionary accumulation pattern.
# We can apply in various scenarios.

# One other example is counting the occurrences of words inside a string.
sentence = "the dog chased the rabbit into the forest but the rabbit was too quick"
word_counts = {}
for word in sentence.split():
    if word not in word_counts:
        word_counts[word] = 0
    word_counts[word] += 1
print(word_counts)
# {'the': 4, 'dog': 1, 'chased': 1, 'rabbit': 2, 'into': 1, 'forest': 1, 'but': 1, 'was': 1, 'too': 1, 'quick': 1}

# We can now iterate through our dictionary and print it in a friendly way.
for word in word_counts:
    print("The word {} was found {} times.".format(word, word_counts[word]))
