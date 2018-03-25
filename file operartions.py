'''text = "Sample text ot save\nNew Line!"

saveFile = open('exampleFile.txt', "w") # w for write

saveFile.write(text)
saveFile.close()'''

'''appendMe = "\nNew line appended"

appendFile = open('exampleFile.txt', "a") # a for append

appendFile.write(appendMe)
appendFile.close()'''

readMe = open("exampleFile.txt", "r") # r for read
#text = readMe.read() #save as string
textList = readMe.readlines() # save as list, one line is one item
#print(text)
print(textList)

readMe.close()
