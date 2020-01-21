import collections.abc

cityNames = ["Paris", "Rennes", "Milano", "Rotterdam", "Dortmund", "London", "Liverpool"]
population = [123, 732, 421, 188, 209, 231, 239]
countries = ["FR", "FR", "IT", "ND", "DE", "UK", "UK"]

cityInfoList = zip(cityNames, population, countries)
# We remember that the zip function returns an iterator of tuples.
print(cityInfoList)  # <zip object at 0x0000013D3A891BC0>
cityInfoList = list(cityInfoList)
print(cityInfoList)
# [('Paris', 123, 'FR'), ('Rennes', 732, 'FR'), ('Milano', 421, 'IT'), ('Rotterdam', 188, 'ND'),
# ('Dortmund', 209, 'DE'), ('London', 231, 'UK'), ('Liverpool', 239, 'UK')]


class City:
    def __init__(self, name, pop, country):
        self.name = name
        self.pop = pop
        self.country = country


cities = list(map(lambda ci: City(ci[0], ci[1], ci[2]), cityInfoList))
print(cities)
# [<__main__.City object at 0x000002077A37C400>, <__main__.City object at 0x000002077A37C940>,
# <__main__.City object at 0x000002077A37CB80>, <__main__.City object at 0x000002077A367BB0>,
# <__main__.City object at 0x000002077A4A7190>, <__main__.City object at 0x000002077A4A71F0>,
# <__main__.City object at 0x000002077A4A7250>]
print(cities[0])  # <__main__.City object at 0x0000026023E7C400>


# We want the City class to be printed in a user-friendly way. This is accomplished by defining an instance method
# named __str__
class City:
    def __init__(self, name, pop, country):
        self.name = name
        self.pop = pop
        self.country = country

    def __str__(self):
        return "[ {} {} {} ]".format(self.name, self.pop, self.country)


cities2 = list(map(lambda ci: City(ci[0], ci[1], ci[2]), cityInfoList))
print(cities2)
# [<__main__.City object at 0x000001E0C8367340>, <__main__.City object at 0x000001E0C83673A0>,
# <__main__.City object at 0x000001E0C8367400>, <__main__.City object at 0x000001E0C8367460>,
# <__main__.City object at 0x000001E0C83674C0>, <__main__.City object at 0x000001E0C8367520>,
# <__main__.City object at 0x000001E0C83675B0>]
print(cities2[0])  # [ Paris 123 FR ]

# We could also use list comprehension:
cities3 = [City(name, pop, country) for (name, pop, country) in cityInfoList]
# cities3 = [City(*t) for t in cityInfoList] - it would also work like this; see packing_and_unpacking_tuples.py
print(isinstance(cities3, collections.abc.Sequence))  # True
print(cities3)
# [<__main__.City object at 0x000001C26F41CB50>, <__main__.City object at 0x000001C26F537670>,
# <__main__.City object at 0x000001C26F5376D0>, <__main__.City object at 0x000001C26F537730>,
# <__main__.City object at 0x000001C26F537790>, <__main__.City object at 0x000001C26F5377F0>,
# <__main__.City object at 0x000001C26F537850>]
print(cities3[0])  # [ Paris 123 FR ]
