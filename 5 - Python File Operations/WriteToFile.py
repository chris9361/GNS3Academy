
newfile = open("c:/newfile.txt", "w")

newfile.write("I like Python.\nDo You?\n")

newfile.close()

newfile = open("c:/newfile.txt", "a")
newfile.write("This is a great day for science!\n")

newfile.close()

newfile = open("c:/newfile.txt", "a")
newfile.writelines(["Cisco", "Juniper", "HP\n"])

newfile.close()

newfile = open("c:/newfile.txt", "a")
newfile.writelines(("Avaya", "Nortal", "Arista\n"))

newfile.close()

