fileName = "testFile.txt"

def WriteFile(fileName, writeText):
    file = open(fileName, "w")
    file.write(writeText)
    file.close()

def ReadFile(fileName):
    file = open(fileName, "r")
    print(file.read())
    print("\n読み終わりました。")
    file.close()
