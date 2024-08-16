#Dictionaries and Sets 
# Creating a dictionary
my_dict = {'name': 'John', 'age': 25, 'location': 'New York'}
print(my_dict)
# Adding a new key-value pair
my_dict['email'] = 'john@example.com'
print(my_dict)
# Updating an existing key-value pair
my_dict['age'] = 26
print(my_dict)
# Remove an item by key
removed_item = my_dict.pop('location')  # Returns 'New York'
print(removed_item)
# Remove an item using del
del my_dict['email']
print(my_dict)
# Accessing an item by key
age = my_dict['age']  # Returns 26
print(age)
# Using the get method to avoid KeyError
name = my_dict.get('name', 'Unknown')  # Returns 'John'
print(name)
# Check if a key exists
if 'name' in my_dict:
    print("Name exists in dictionary")

#Sets 
# Creating a set
my_set = {'apple', 'banana', 'cherry'}
print(my_set)
# Add an element to the set
my_set.add('orange')
print(my_set)
# Remove an element from the set
my_set.remove('banana')  # Raises KeyError if the element is not found
print(my_set)
# Using discard to remove an element without raising an error if the element is not found
my_set.discard('kiwi')
print(my_set)
# Check if an element is in the set
if 'apple' in my_set:
    print("Apple is in the set")

# Union of sets
set_a = {'apple', 'banana', 'cherry'}
set_b = {'cherry', 'date', 'elderberry'}
union_set = set_a | set_b  # Returns {'apple', 'banana', 'cherry', 'date', 'elderberry'}
print(union_set)
# Intersection of sets
intersection_set = set_a & set_b  # Returns {'cherry'}
print(intersection_set)
# Difference of sets
difference_set = set_a - set_b  # Returns {'apple', 'banana'}
print(difference_set)