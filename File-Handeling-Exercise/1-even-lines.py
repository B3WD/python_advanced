import re

with open("texts/text_1.txt" ,) as file:
    lines = file.readlines()

for i, line in enumerate(lines):
    if i % 2 == 0:
        line = re.sub(r"[\-,\.!?]", "@", line)
        line = line.split()[::-1]
        print(" ".join(line))