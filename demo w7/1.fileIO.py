
def read_file(filename="FileToSend.txt", mode="r"):
    with open(filename, mode=mode) as file:
        while True:
            content = file.read(1000)
            if content:
                print("new line: ", content)
                print(type(content))
            else:
                break


# # read file
# read_file(mode="r")
#
#
# # read file as bytes
# read_file(mode="rb")


'''
write file
'''
# with open("fileToWrite.txt", "w+") as file:
#     content = "COMP3331"
#     file.write(content)


'''
write file with bytes
'''
with open("fileToWrite_bytes.txt", "wb+") as file:
    content = b"this is byte format"
    file.write(content)







