# Sequences can be concatenated with the + operator and
# repeated with the * operator:
s1 = "abcd"
s2 = "efgh"
print(s1 + s2)  # abcdefgh
print(s1 * 3)  # abcdabcdabcd
l1 = [1, 2, 3]
l2 = [4, 5, 6]
print(l1 + l2)  # [1, 2, 3, 4, 5, 6]
print(l1 * 2)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]
t1 = (4, 5, 6, 7)
t2 = (8, 9, 10)
print(t1 + t2)  # (4, 5, 6, 7, 8, 9, 10)
print(t1 * 2)  # (4, 5, 6, 7, 4, 5, 6, 7)
