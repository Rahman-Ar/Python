#Regular Expressions
import re

text = "The rain in Spain falls mainly on the plain."

match = re.search(r'rain', text)
if match:
    print("Found:", match.group())

match = re.match(r'The', text)
if match:
    print("Matched:", match.group())

matches = re.findall(r'\b\w{5}\b', text)
print("All matches:", matches)

#Extracting & Grouping
text = "Contact: John Doe, Phone: 123-456-7890"

# Using groups
match = re.search(r'(\w+)\s(\w+),\sPhone:\s(\d{3})-(\d{3})-(\d{4})', text)
if match:
    first_name = match.group(1)
    last_name = match.group(2)
    phone = match.group(3) + '-' + match.group(4) + '-' + match.group(5)
    print(f"Name: {first_name} {last_name}, Phone: {phone}")

#Replacing Text
text = "The rain in Spain falls mainly on the plain."

# Replace all instances of 'ain' with '***'
replaced_text = re.sub(r'ain', '***', text)
print(replaced_text)

