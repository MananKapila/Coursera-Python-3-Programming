# All these methods mutate the list they are called from (except for *count* and *index*, of course)

# The *append* method adds an element to the end of the list.
lst = []
# ======= Memory =======
# lst    ----- []
# ======================
lst.append("hi")
lst.append("there")
lst.append("this")
lst.append("is")
lst.append("me")
# ======= Memory =======
# lst    ----- ['hi', 'there', 'this', 'is', 'me']
# ======================
print(lst)

# The *insert* method inserts an element at a specified index: list.insert(<index>, <element>)
lst.insert(2, "cutie")
# ======= Memory =======
# lst    ----- ['hi', 'there', 'cutie', 'this', 'is', 'me']
# ======================
print(lst)

# The *count* function counts the number of occurences of one element inside the list
lst.append("hi")
# ======= Memory =======
# lst    ----- ['hi', 'there', 'cutie', 'this', 'is', 'me', 'hi']
# ======================
print(lst.count("hi"))  # 2
print(lst.count("ok"))  # 0
print(lst.count("me"))  # 1

# The *index* method returns the first index where a specified element is found in the list
print(lst.index("hi"))  # 0
# print(lst.index("ok"))  # ValueError: 'ok' is not in list

# The *reverse* method replaces the list in memory with its reverse form (it does NOT create a new list)
lst.reverse()
# ======= Memory =======
# lst    ----- ['hi', 'me', 'is', 'this', 'cutie', 'there', 'hi']
# ======================
print(lst)

# The *sort* method replaces the list in memory with its sorted form (it does NOT create a new list)
lst.sort()
# ======= Memory =======
# lst    ----- ['cutie', 'hi', 'hi', 'is', 'me', 'there', 'this']
# ======================
print(lst)

# The *remove* method removes THE FIRST occurrence of an item
lst.remove("hi")
# ======= Memory =======
# lst    ----- ['cutie', 'hi', 'is', 'me', 'there', 'this']
# ======================
print(lst)
lst.remove("hi")
# ======= Memory =======
# lst    ----- ['cutie', 'is', 'me', 'there', 'this']
# ======================
print(lst)

# The *pop* method can do two things.
# When it's called without parameters, it removes and returns the last element of the list.
element = lst.pop()
# ======= Memory =======
# lst    ----- ['cutie', 'is', 'me', 'there']
# ======================
print(element)  # this
print(lst)
# When an index is passed as parameter, *pop* removes and returns the element inside the list at that particular index.
element = lst.pop(2)
# ======= Memory =======
# lst    ----- ['cutie', 'is', 'there']
# ======================
print(element)  # me
print(lst)