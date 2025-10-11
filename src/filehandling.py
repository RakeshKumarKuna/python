def readingFile():
    file=open("D:/AI/Python/resources/textfile.txt",mode="r")
    print(file.readlines())

# doing operations with file using with open
def readingFilewithopen():
    with open("D:/AI/Python/resources/textfile.txt",mode="r+") as file:
        data=file.readlines()
        print(data)
        print("="*45)
        file.write("currently i am learning python")
        print(file.readlines())

#readingFile()
readingFilewithopen()