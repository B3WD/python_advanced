import re


with open("texts/text_1.txt", "r") as file:
    lines = file.readlines()

with open("texts/output-2.txt", "w") as file2:
    for i, line in enumerate(lines):
        punc_cunt = len(re.findall(r"[\-,\.'!?]", line))
        chars = len(re.findall(r"[\w]", line))
        edited_line = f"Line {i + 1}: {line[0:-2]} ({chars})({punc_cunt})\n"
        file2.write(edited_line)
