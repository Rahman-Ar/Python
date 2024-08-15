#Functions

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
num = int(input("Enter a number: "))
if is_even(num):
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")

# calling function with parameters
def describe_person(name, age, city="Unknown"):
    description = f"{name} is {age} years old and lives in {city}."
    return description

person1 = describe_person("Abdul", 22, "India")
print(person1)

person2 = describe_person(name="Bob", age=30)
print(person2)
    