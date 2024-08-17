#String Manipulation 
text = "Hello, World!"
substring = text[0:5]
print(substring)
substring = text[7:12]
print(substring)
last_char = text[-1]
print(last_char)

#String concatinate
greeting = "Hello"
name = "Abdul"
message = greeting + ", " + name + "!"
print(message)

#String Formatting
name = "Abdul"
age = 22
introduction = f"My name is {name} and I am {age} years old."
print(introduction)

introduction = "My name is {} and I am {} years old.".format(name, age)
print(introduction)

introduction = "My name is %s and I am %d years old." % (name, age)
print(introduction)

text = "Hello, World!"
lower_case = text.lower()
print(lower_case) 

upper_case = text.upper()
print(upper_case)

def is_palindrome(text):
    clean_text = text.replace(" ", "").lower()
    return clean_text == clean_text[::-1]

text = "A man a plan a canal Panama"
print(is_palindrome(text)) 

text = "Hello"
print(is_palindrome(text))
            