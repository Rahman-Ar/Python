#list comprehensions
#creating a list of squares
squares = [x**2 for x in range(10)]
print(squares)

#printing even numbers
even_num = [x for x in range(10) if x % 2 == 0 ]
print(even_num)

words = ["hello", "world", "python"]
uppercase_word = [word.upper() for word in words]
print(uppercase_word)

#nested list
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

flattened = [item for row in matrix for item in row]
print(flattened)