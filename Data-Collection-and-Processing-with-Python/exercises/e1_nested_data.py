# In python, we can have nested data structures, such as a list of dictionaries or a dictionary of lists of
# dictionaries, etc.

# Let's see some example exercises.

animals = [['cat', 'dog', 'mouse'], ['horse', 'cow', 'goat'], ['cheetah', 'giraffe', 'rhino']]
# Use indexing to assign the element ‘horse’ to the variable name <idx1>.
idx1 = animals[1][0]
print(idx1)  # horse

data = ['bagel', 'cream cheese', 'breakfast', 'grits', 'eggs', 'bacon', [34, 9, 73, []],
        [['willow', 'birch', 'elm'], 'apple', 'peach', 'cherry']]
# Using indexing, retrieve the string ‘willow’ from the list and assign that to the variable <plant>.
plant = data[7][0][0]
print(plant)  # willow

info = {'personal_data':
            {'name': 'Lauren',
             'age': 20,
             'major': 'Information Science',
             'physical_features':
                 {'color': {'eye': 'blue',
                            'hair': 'brown'},
                  'height': "5'8"}
             },
        'other':
            {'favorite_colors': ['purple', 'green', 'blue'],
             'interested_in': ['social media', 'intellectual property', 'copyright', 'music', 'books']
             }
        }
# Extract the value associated with the key 'color' and assign it to the variable <color>.
color = info['personal_data']['physical_features']['color']
print(color)  # {'eye': 'blue', 'hair': 'brown'}
