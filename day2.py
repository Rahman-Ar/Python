#Control Flow
mark = int(input("Enter your mark: "))

if mark >= 90:
    grade = 'A'
elif mark >= 80:
    grade = 'B'
elif mark >= 70:
    grade = 'C'
elif mark >= 60:
    grade = 'D'
else:
    grade = 'E'
    
print(f"Your grade is {grade}")

num = [10,60,29,69,62]

for i in num:
    print(f"Number {i}")


numbers = [1, 2, 3, 4, 5]
index = 0

while index < len(numbers):
    print(f"Number: {numbers[index]}")
    index += 1
    