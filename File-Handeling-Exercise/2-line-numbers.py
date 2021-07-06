import re


with open("texts/text_1.txt", "r") as source:
    dest = open("texts/output-2.txt", "w")

    for i, line in enumerate(source):
        punc_cunt = len(re.findall(r"[\-,\.'!?]", line))
        chars = len(re.findall(r"[\w]", line))
        edited_line = f"Line {i + 1}: {line[0:-2]} ({chars})({punc_cunt})\n"
        dest.write(edited_line)

    dest.close()