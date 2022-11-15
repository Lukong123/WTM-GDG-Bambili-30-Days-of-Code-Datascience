# opening a file
file = open('dog_breeds.txt')

# closing a file there are two methods
## using try finally

# reader = open('dog_breeds.txt')
# try:
#     # more processes
# finally:
#     reader.close()

## using with statement
with open('dog_breeds.txt', 'r') as reader:
    # further processsing here
    print('good')

## readeing and writting opened files
with open('dog_breeds.txt', 'r') as reader:
    print(reader.read())
    print(reader.readline(5))
    print(reader.readline(5))
    print(reader.readline(5))
    print(reader.readline(5))
    print(reader.readline(5))

# reading a file as a list
f = open('dog_breeds.txt')
f.readlines()  # Returns a list object

# looping
with open('dog_breeds.txt', 'r') as reader:
    line = reader.readline()
    while line != '':
        print(line, end='')
        line = reader.readline()

# for loop
with open('dog_breeds.txt', 'r') as reader:
    for line in reader:
        print(line, end='')