# As we saw in e19, this situation basically creates a clone of the list x is pointing to.
x = [1, 2, 3, 4]
y = [1, 2, 3, 4]
# ======= Memory =======
# x    ----- [1, 2, 3, 4]
# y    ----- [1, 2, 3, 4]
# ======================
# But perhaps we want to clone a list without having to explicitly rewrite all the values in it.
# We can do that using slices.
x = [1, 2, 3, 4]
y = x[:]  # this selects the maximum slice, which is the whole sequence
# ======= Memory =======
# x    ----- [1, 2, 3, 4]
# y    ----- [1, 2, 3, 4]
# ======================
# We can check that this cloning worked, by modifying y and checking that x remained intact.
y[0] = 100
print(y)  # [100, 2, 3, 4]
print(x)  # [1, 2, 3, 4]
