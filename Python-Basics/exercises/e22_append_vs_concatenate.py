# As we've seen in e21, the *append* method adds an element to the end of a list, by mutating that list in memory.
lst = [42, 54, 38]
# ======= Memory =======
# lst    ----- [42, 54, 38]
# ======================
lst.append(13)
print(lst)  # [42, 54, 38, 13]
# ======= Memory =======
# lst    ----- [42, 54, 38, 13]
# ======================

# We also know that we can concatenate two lists. This can add one or more elements to the end of a list.
# However, concatenation (done with the + sign) does NOT MUTATE existing lists, but creates new lists in memory.
con = lst + [22, 77]
# ======= Memory =======
# lst    ----- [42, 54, 38, 13]
# con    ----- [42, 54, 38, 13, 22, 77]
# ======================
print(lst)  # [42, 54, 38, 13]
print(con)  # [42, 54, 38, 13, 22, 77]
# If we want to see the concatenation's effects on the list we concatenate on, we need to assign the result
# to the respective list itself.
lst = lst + [11]
# ======= Memory =======
#              [42, 54, 38, 13, 11]
# lst    ____/ [42, 54, 38, 13]         (this list in memory gets lost, because it's not assigned to anything anymore)
# con    ----- [42, 54, 38, 13, 22, 77]
# ======================
print(lst)  # [42, 54, 38, 13, 11]
print(con)  # [42, 54, 38, 13, 22, 77]

# There is an important particularity of the Python language, when it comes to concatenation of strings.
# We know that for integers, x += 1 is equivalent with x = x + 1
# However, when we do this on lists, += has a completely different meaning.
# lst += [1,2] does NOT CONCATENATE lst with [1,2] (that would create a new, longer list in memory and point lst to it)
# Instead, it MUTATES lst by adding new elements to the existing list in memory, the one lst was already pointing to.
# Basically, += behaves like the append method.
# In order to better see the difference between + and +=, let's analyze these two examples:

lst = [0, 0, 0]
# ======= Memory =======
# lst    ----- [0, 0, 0]
# ======================
alias = lst
# ======= Memory =======
# lst    ----- [0, 0, 0]
# alias  ____/
# ======================

# ---------------- Example 1 ----------------
lst = lst + [1, 2]
# ======= Memory =======
#             [0, 0, 0, 1, 2]
# lst    ___/ [0, 0, 0]
# alias  ____/
# ======================
print(lst)  # [0, 0, 0, 1, 2]
print(alias)  # [0, 0, 0]
# We can see that this concatenation created a new list in memory and pointed lst to that new memory location
# (because this is how concatenation works).
# Consequently, lst and its former alias don't refer to the same list in memory anymore.

# Let's reinitialize our base case.
lst = [0, 0, 0]
alias = lst
# ======= Memory =======
# lst    ----- [0, 0, 0]
# alias  ____/
# ======================

# ---------------- Example 2 ----------------
lst += [1, 2]
# ======= Memory =======
# lst    ----- [0, 0, 0, 1, 2]
# alias  ____/
# ======================
print(lst)  # [0, 0, 0, 1, 2]
print(alias)  # [0, 0, 0, 1, 2]
# We notice how += did NOT create a new list in memory to assign to lst, but MUTATED the list lst was already
# pointing to. As a consequence, this change can be seen by inspecting all aliases of lst.

# We remember that the alias of a variable is another variable pointing to the same location in memory.


# So far, everything we've seen in e21 and e22 mutates lists, except for the *count* and *index* methods
# and concatenation.
# (Remember that += is NOT a concatenation.)
