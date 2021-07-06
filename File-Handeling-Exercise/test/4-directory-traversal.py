from os import path, listdir


def traverse(startDest):
    all = listdir(startDest)
    dirs, files = [], []

    for x in all:
        if path.isfile(path.join(startDest, x)):
            files.append(x)
        else:
            dirs.append(x)

    print(files)

    for dir in dirs:
        dir = path.join(startDest, dir)
        traverse(dir)


traverse(input())