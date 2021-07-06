import shutil
from os import mkdir, chdir, path, remove


def createFile(name, dest=""):
    f = open(path.join(dest, name), "w")
    f.close()

def writeInFile(msg, dest):
    with open(dest, "a") as f:
        f.write(msg + "\n")


def replaceString(newStr, oldStr, dest):
    if not path.exists(dest):
        print("An error occurred")
        return

    tmpPath, ext = dest.split(".")
    tmpFile = tmpPath + "-Copy." + ext
    createFile(tmpFile)

    with open(dest, "r") as f:
        tmpF = open(tmpFile, "w")

        for line in f:
            tmpF.write(line.replace(oldStr, newStr))

        tmpF.close()

    with open(dest, "w") as f:
        tmpF = open(tmpFile, "r")

        for line in tmpF:
            f.write(line)

        tmpF.close()

    deleteFile(tmpFile)

def deleteFile(dest):
    if not path.exists(dest):
        print("An error occurred")
        return

    remove(dest)

def prog():
    while True:
        command = input()

        if command == "End":
            break
        
        action, ops = command.split('-', maxsplit=1)

        if action == "Create":
            createFile(ops)

        elif action == "Add":
            dest, msg = ops.split('-')
            writeInFile(msg, dest)

        elif action == "Replace":
            dest, oldStr, newStr = ops.split('-')
            replaceString(newStr, oldStr, dest)

        elif action == "Delete":
            deleteFile(ops)


prog()