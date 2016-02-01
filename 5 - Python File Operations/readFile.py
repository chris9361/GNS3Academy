
myfile = open('c:/router.txt', 'r')
#  modes = r, w, a, b

myfile.seek(0)

for line in myfile.readlines():
    if line.startswith("A"):
        print(line)