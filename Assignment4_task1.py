try:
    with open("sample.txt","rt") as file:
        for line in file:
            print(line.rstrip('\n'))
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found")
else:
    with open("sample.txt","wt") as file:
        file.write("Reading file content:\nLine 1: this is a sample text file.\nLine 2: it contain multiple lines.\n")

#creating a file
#a=open("sample.txt","xt")
#print(a)