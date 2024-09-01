import pandas as pd

# Read CSV file
df = pd.read_csv('data.csv')

# Process data (e.g., display first few rows)
print(df.head())

# Write DataFrame to CSV file
df.to_csv('output.csv', index=False)
import csv

# Read CSV file
with open('data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)

# Write to CSV file
with open('output.csv', 'w', newline='') as csvfile:
    fieldnames = ['column1', 'column2']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'column1': 'value1', 'column2': 'value2'})

import pandas as pd

# Read Excel file
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')

# Process data (e.g., display first few rows)
print(df.head())

# Write DataFrame to Excel file
df.to_excel('output.xlsx', sheet_name='Sheet1', index=False)

import xml.etree.ElementTree as ET

# Parse XML file
tree = ET.parse('data.xml')
root = tree.getroot()

# Process XML data
for child in root:
    print(child.tag, child.attrib)
    for subchild in child:
        print(subchild.tag, subchild.text)
