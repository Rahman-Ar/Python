#File Handling
file = open('example.txt', 'w')
file.write('Hello, world!\n')
file.close()                     

#reading a file
file = open('example.txt', 'r')
content = file.read()            
print(content)
file.close()

#writing into a existing file
file = open('example.txt', 'w')  
file.write('Hello, world!\n')    
file.write('Another line.\n')    
file.close()                    