# Objects and references

# Two references pointing to two equivalent immutable objects point to the SAME object (the same location in memory).
a = "hello"
b = "hello"
# ======= Memory =======
# a    ----- "hello"
# b    ____/
# ======================
# The *is* operator verifies whether two references point to the same object/location in memory
# (aka the two references are aliases of each other).
print(a is b)  # True
# The *id* function prints a unique identified of the object a reference is pointing towards
# (based on the object's location in memory).
print(id(a))  # 2034429399792
print(id(b))  # 2034429399792

# Two references pointing to two equivalent mutable objects point to DIFFERENT object
# (with different locations in memory).
x = [1, 2, 3, 4]
y = [1, 2, 3, 4]
# ======= Memory =======
# x    ----- [1, 2, 3, 4]
# y    ----- [1, 2, 3, 4]
# ======================
# Even though lst1 and lst2 point to equivalent objects, they don't point to the SAME object, ...
print(x is y)  # False (they are not aliases)
print(x == y)  # True
# ... as they have different locations in memory.
print(id(x))  # 1973669252992
print(id(y))  # 1973669015296
# We can say that y is a clone of x.
# However, we can point b to the same object that a is pointing to.
y = x
# ======= Memory =======
# x    ----- [1, 2, 3, 4]
# y    ____/ [1, 2, 3, 4]
# ======================
# Now, x and y are aliases.
print(a is b)  # True
# Consequently, if we modify the object that y is pointing to, we can notice that change by inspecting x.
y[0] = 100
# ======= Memory =======
# x    ----- [100, 2, 3, 4]
# y    ____/ [1, 2, 3, 4]
# ======================
print(x)  # [100, 2, 3, 4]
