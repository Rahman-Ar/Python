#Lists and Tuples 
my_list = [1, 2, 3, 4, 5]
print(my_list[0])
print(my_list[-1])
my_list[2] = 10
print(my_list)
my_list.append(6)
print(my_list) 

my_list.insert(2, 7)
print(my_list)
my_list.remove(10)
print(my_list) 

my_list.pop() 
print(my_list) 

#Tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[0])  # Output: 1
print(my_tuple[-1]) # Output: 5
# This will raise an error because tuples cannot be modified
# my_tuple[2] = 10

# However, you can create a new tuple with modified values
new_tuple = my_tuple[:2] + (10,) + my_tuple[3:]
print(new_tuple)  # Output: (1, 2, 10, 4, 5)
