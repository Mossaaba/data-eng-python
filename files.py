
### Reading an entire file
filename= "journal.txt"
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line)

## Writing to a file
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

### Appending to a file
filename = 'journal.txt'
with open(filename , 'a') as file_object:
    file_object.write("\n\n The text was generate by lipsum.\n")
