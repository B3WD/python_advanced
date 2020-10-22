# correcting mistakes in someone's code

numbers_dictionary = {}

while True:
    line = input()

    if line == "Search":
        break

    try:    
        number = int(input())
    except ValueError:
        print("The variable number must be an integer")
        continue
    
    key = line
    numbers_dictionary[key] = number


while True:
    line = input()

    if line == "Remove":
        break

    searched = line

    try:
        print(numbers_dictionary[searched])
    except KeyError:
        print(f"Number does not exist in the dictionary")


while True:
    line = input()

    if line == "End":
        break

    searched = line
    
    try:
        del numbers_dictionary[searched]
    except KeyError:
        print(f"Number does not exist in the dictionary")

print(numbers_dictionary)