import re


with open("texts/text_1.txt", 'r') as file:
    for i, line in enumerate(file):
        if i % 2 == 0:
            line = re.sub(r"[\-,\.!?]", "@", line)
            line = line.split()[::-1]
            print(" ".join(line))